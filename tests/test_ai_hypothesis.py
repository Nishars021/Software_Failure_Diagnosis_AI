import os

from src.ai_hypothesis import generate_ai_hypotheses


problem = "The web application suddenly started returning HTTP 500 errors."


print("AI HYPOTHESIS TEST")
print("=" * 60)

if not os.getenv("OPENAI_API_KEY"):
    print("SKIPPED: OPENAI_API_KEY is not configured.")
    print("Using the local hypothesis generator instead.")
else:
    hypotheses = generate_ai_hypotheses(problem)

    print(f"Generated: {len(hypotheses)} hypotheses")

    for hypothesis in hypotheses:
        print(f"{hypothesis.id}: {hypothesis.cause}")