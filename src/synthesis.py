from src.hypothesis import Hypothesis
from src.decision import are_compatible
from src.scoring import HypothesisScore


def combine_hypotheses(
    h1: Hypothesis,
    h2: Hypothesis,
    score1: HypothesisScore,
    score2: HypothesisScore
):
    """
    Create a combined hypothesis when two hypotheses are
    compatible and both have meaningful supporting evidence.
    """

    # Both hypotheses need positive supporting evidence
    if score1.raw_score <= 0 or score2.raw_score <= 0:
        return None

    # They must be compatible
    if not are_compatible(h1, h2):
        return None

    combined_id = f"COMBINED_{h1.id}_{h2.id}"

    combined_cause = (
        f"{h1.cause} and {h2.cause} may jointly contribute "
        "to the failure"
    )

    assumptions = list(dict.fromkeys(
        h1.assumptions + h2.assumptions
    ))

    predicted_effects = list(dict.fromkeys(
        h1.predicted_effects + h2.predicted_effects
    ))

    required_evidence = list(dict.fromkeys(
        h1.required_evidence + h2.required_evidence
    ))

    return Hypothesis(
        id=combined_id,
        cause=combined_cause,
        assumptions=assumptions,
        predicted_effects=predicted_effects,
        required_evidence=required_evidence
    )