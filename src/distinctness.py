from src.hypothesis import Hypothesis


def calculate_distinctness(h1: Hypothesis, h2: Hypothesis):
    """
    Compare two hypotheses across multiple axes.

    Returns a score between 0 and 1.
    1.0 = highly different
    0.0 = essentially identical
    """

    scores = {}

    # 1. Compare causes
    scores["cause"] = 1.0 if h1.cause.lower() != h2.cause.lower() else 0.0

    # 2. Compare assumptions
    assumptions_1 = set(a.lower() for a in h1.assumptions)
    assumptions_2 = set(a.lower() for a in h2.assumptions)

    scores["assumptions"] = (
        1.0 if assumptions_1 != assumptions_2 else 0.0
    )

    # 3. Compare predicted effects
    effects_1 = set(e.lower() for e in h1.predicted_effects)
    effects_2 = set(e.lower() for e in h2.predicted_effects)

    scores["predicted_effects"] = (
        1.0 if effects_1 != effects_2 else 0.0
    )

    # 4. Compare required evidence
    evidence_1 = set(e.lower() for e in h1.required_evidence)
    evidence_2 = set(e.lower() for e in h2.required_evidence)

    scores["required_evidence"] = (
        1.0 if evidence_1 != evidence_2 else 0.0
    )

    # Average across the four axes
    overall_score = sum(scores.values()) / len(scores)

    return {
        "overall_score": overall_score,
        "axis_scores": scores
    }