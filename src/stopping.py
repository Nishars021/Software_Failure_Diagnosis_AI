from typing import List

from src.scoring import HypothesisScore
from src.budget import InvestigationBudget


def should_stop(
    scores: List[HypothesisScore],
    budget: InvestigationBudget
) -> tuple[bool, str]:

    # 1. Check investigation rounds
    if budget.budget_exhausted():
        return True, "Investigation budget exhausted."

    # 2. Remove UNKNOWN from normal ranking
    valid_scores = [
        score
        for score in scores
        if score.hypothesis_id != "UNKNOWN"
    ]

    if not valid_scores:
        return True, "No usable hypotheses remain."

    # 3. Rank hypotheses
    ranked = sorted(
        valid_scores,
        key=lambda x: x.confidence,
        reverse=True
    )

    best = ranked[0]

    # 4. Insufficient evidence comes BEFORE tie checking
    if best.confidence < 50:
        return True, (
            "Available evidence is insufficient "
            "to support any known hypothesis."
        )

    # 5. Strong hypothesis
    if best.confidence >= 75:

        if len(ranked) == 1:
            return True, (
                "A strong hypothesis has been identified."
            )

        second = ranked[1]

        if best.confidence - second.confidence >= 15:
            return True, (
                "A strong hypothesis clearly leads."
            )

    # 6. Close hypotheses
    if len(ranked) >= 2:

        second = ranked[1]

        if abs(
            best.confidence - second.confidence
        ) <= 10:

            return True, (
                "Top hypotheses are sufficiently close; "
                "move to synthesis or a discriminating test."
            )

    # 7. Continue investigation
    return False, "Investigation can continue."