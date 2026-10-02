from src.hypothesis import Hypothesis
from src.distinctness import calculate_distinctness


MIN_DISTINCTNESS_SCORE = 0.50


def validate_hypothesis(hypothesis: Hypothesis) -> bool:
    """
    Check whether a hypothesis contains the required information.
    """

    if not hypothesis.id:
        return False

    if not hypothesis.cause:
        return False

    if not hypothesis.assumptions:
        return False

    if not hypothesis.predicted_effects:
        return False

    if not hypothesis.required_evidence:
        return False

    return True


def validate_hypotheses(hypotheses):
    """
    Validate and filter a list of hypotheses.

    UNKNOWN is always preserved.
    """

    valid = []
    seen_ids = set()
    seen_causes = set()

    for hypothesis in hypotheses:

        # --------------------------------------------------
        # Basic structure validation
        # --------------------------------------------------
        if not validate_hypothesis(hypothesis):
            continue

        # --------------------------------------------------
        # UNKNOWN is handled separately
        # --------------------------------------------------
        if hypothesis.id == "UNKNOWN":
            continue

        # --------------------------------------------------
        # Duplicate ID check
        # --------------------------------------------------
        if hypothesis.id in seen_ids:
            continue

        # --------------------------------------------------
        # Duplicate cause check
        # --------------------------------------------------
        cause_key = hypothesis.cause.lower().strip()

        if cause_key in seen_causes:
            continue

        # --------------------------------------------------
        # Multi-axis distinctness check
        # --------------------------------------------------
        is_distinct = True

        for existing in valid:

            result = calculate_distinctness(
                existing,
                hypothesis
            )

            if result["overall_score"] < MIN_DISTINCTNESS_SCORE:
                is_distinct = False
                break

        if not is_distinct:
            continue

        valid.append(hypothesis)
        seen_ids.add(hypothesis.id)
        seen_causes.add(cause_key)

    # ------------------------------------------------------
    # Always preserve UNKNOWN
    # ------------------------------------------------------
    unknown = next(
        (
            hypothesis
            for hypothesis in hypotheses
            if hypothesis.id == "UNKNOWN"
        ),
        None
    )

    if unknown is not None:
        valid.append(unknown)

    return valid