from typing import List

from src.scoring import HypothesisScore
from src.budget import InvestigationBudget


def should_stop(
    scores: List[HypothesisScore],
    budget: InvestigationBudget
) -> tuple[bool, str]:

    # Rule 1: Budget exhausted
    if budget.budget_exhausted():
        return True, "Investigation budget exhausted."

    valid_scores = [
        score
        for score in scores
        if score.hypothesis_id != "UNKNOWN"
    ]

    if not valid_scores:
        return True, "No usable hypotheses remain."

    ranked = sorted(
        valid_scores,
        key=lambda x: x.confidence,
        reverse=True
    )

    best = ranked[0]

    # Rule 2: Strong winner
    if best.confidence >= 75:
        if len(ranked) == 1:
            return True, "A strong hypothesis has been identified."

        second = ranked[1]

        if best.confidence - second.confidence >= 15:
            return True, "A strong hypothesis clearly leads."

    # Rule 3: Close hypotheses
    if len(ranked) >= 2:
        second = ranked[1]

        if abs(best.confidence - second.confidence) <= 10:
            return True, "Top hypotheses remain difficult to distinguish."

    # Rule 4: No hypothesis has enough support
    if best.confidence < 50:
        return True, "Available evidence is insufficient."

    return False, "Investigation can continue."