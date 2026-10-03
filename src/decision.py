from dataclasses import dataclass
from typing import List

from src.scoring import HypothesisScore


@dataclass
class Decision:
    outcome: str
    selected_hypotheses: List[str]
    explanation: str


def make_decision(
    scores: List[HypothesisScore],
    hypotheses=None
) -> Decision:

    if not scores:
        return Decision(
            outcome="ABSTAIN",
            selected_hypotheses=[],
            explanation="No hypotheses were available for evaluation."
        )

    # Ignore UNKNOWN when comparing normal hypotheses
    valid_scores = [
        score for score in scores
        if score.hypothesis_id != "UNKNOWN"
    ]

    if not valid_scores:
        return Decision(
            outcome="ABSTAIN",
            selected_hypotheses=[],
            explanation=(
                "No known hypothesis has sufficient supporting evidence. "
                "The cause may be unknown."
            )
        )

    # Sort by confidence
    ranked = sorted(
        valid_scores,
        key=lambda x: x.confidence,
        reverse=True
    )

    best = ranked[0]

    # --------------------------------------------------
    # CASE 1: Evidence is too weak
    # --------------------------------------------------
    # IMPORTANT:
    # Check this BEFORE the tie condition.
    #
    # Otherwise two weak hypotheses such as
    # H1 = 10% and H2 = 8%
    # would incorrectly produce TEST.
    # --------------------------------------------------

    if best.confidence < 50:

        return Decision(
            outcome="ABSTAIN",
            selected_hypotheses=[],
            explanation=(
                "None of the known hypotheses has sufficient "
                "supporting evidence. The cause may be unknown."
            )
        )

    # --------------------------------------------------
    # CASE 2: Strong single hypothesis
    # --------------------------------------------------

    if best.confidence >= 50:

        if len(ranked) == 1:
            return Decision(
                outcome="SELECT",
                selected_hypotheses=[best.hypothesis_id],
                explanation=(
                    f"{best.hypothesis_id} has sufficient supporting "
                    f"evidence and no competing hypothesis has comparable support."
                )
            )

        second = ranked[1]

        margin = best.confidence - second.confidence

        if margin >= 15:
            return Decision(
                outcome="SELECT",
                selected_hypotheses=[best.hypothesis_id],
                explanation=(
                    f"{best.hypothesis_id} has the strongest evidence "
                    f"with a confidence margin of {margin:.2f} points."
                )
            )
        second = ranked[1]

        if best.confidence - second.confidence >= 15:

            return Decision(
                outcome="SELECT",
                selected_hypotheses=[best.hypothesis_id],
                explanation=(
                    f"{best.hypothesis_id} is substantially better "
                    f"supported than the other hypotheses."
                )
            )

    # --------------------------------------------------
    # CASE 3: Two reasonably supported hypotheses are close
    # --------------------------------------------------

    if len(ranked) >= 2:

        second = ranked[1]

        difference = abs(
            best.confidence - second.confidence
        )

        if difference <= 10:

            return Decision(
                outcome="TEST",
                selected_hypotheses=[
                    best.hypothesis_id,
                    second.hypothesis_id
                ],
                explanation=(
                    f"{best.hypothesis_id} and {second.hypothesis_id} "
                    f"remain difficult to distinguish. "
                    f"A discriminating test is recommended."
                )
            )

    # --------------------------------------------------
    # CASE 4: Evidence is not strong enough
    # --------------------------------------------------

    return Decision(
        outcome="ABSTAIN",
        selected_hypotheses=[],
        explanation=(
            "The available evidence is insufficient to make "
            "a reliable selection."
        )
    )

def are_compatible(h1, h2) -> bool:
    """
    Determine whether two hypotheses can potentially
    be true at the same time.

    V0.1 uses a simple rule-based approach.
    """

    cause_1 = h1.cause.lower()
    cause_2 = h2.cause.lower()

    # Clearly incompatible pairs
    incompatible_pairs = [
        ("database failure", "database healthy"),
        ("recent deployment", "no recent deployment"),
    ]

    for cause_a, cause_b in incompatible_pairs:
        if (
            (cause_a in cause_1 and cause_b in cause_2)
            or
            (cause_b in cause_1 and cause_a in cause_2)
        ):
            return False

    # By default, different causes are considered
    # potentially compatible.
    return True

def synthesize_hypotheses(h1, h2, score1, score2) -> Decision:
    """
    Combine two compatible hypotheses when both have
    meaningful supporting evidence.
    """

    if not are_compatible(h1, h2):
        return Decision(
            outcome="TEST",
            selected_hypotheses=[h1.id, h2.id],
            explanation=(
                f"{h1.id} and {h2.id} appear incompatible, "
                "so a discriminating test is required."
            )
        )

    return Decision(
        outcome="COMBINE",
        selected_hypotheses=[h1.id, h2.id],
        explanation=(
            f"{h1.id} and {h2.id} are compatible and both "
            f"have supporting evidence. Together they may "
            f"provide a stronger explanation of the failure."
        )
    )