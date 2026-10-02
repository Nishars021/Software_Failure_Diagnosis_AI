import json
import os

from openai import OpenAI

from src.hypothesis import Hypothesis


def generate_ai_hypotheses(problem: str):

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY is not set. "
            "Set your API key before running the AI generator."
        )

    client = OpenAI(api_key=api_key)

    prompt = f"""
You are a software failure diagnosis assistant.

Analyze this software failure:

{problem}

Generate 4 to 6 genuinely different possible causes.

The hypotheses must be meaningfully different, not duplicate
wordings of the same cause.

Also include an UNKNOWN hypothesis representing the possibility
that the true cause is not among the generated hypotheses.

Return ONLY valid JSON in this exact structure:

{{
  "hypotheses": [
    {{
      "id": "H1",
      "cause": "...",
      "assumptions": ["...", "..."],
      "predicted_effects": ["...", "..."],
      "required_evidence": ["...", "..."]
    }}
  ]
}}

Requirements:

- Generate different causal explanations.
- Include assumptions.
- Include observable predicted effects.
- Include evidence that would help distinguish the hypothesis.
- Do not rank the hypotheses.
- Do not assign confidence scores.
- Do not give a final diagnosis.
"""

    response = client.responses.create(
        model="gpt-6-luna",
        input=prompt
    )

    text = response.output_text

    data = json.loads(text)

    hypotheses = []

    for item in data["hypotheses"]:

        hypotheses.append(
            Hypothesis(
                id=item["id"],
                cause=item["cause"],
                assumptions=item.get("assumptions", []),
                predicted_effects=item.get(
                    "predicted_effects",
                    []
                ),
                required_evidence=item.get(
                    "required_evidence",
                    []
                )
            )
        )

    return hypotheses