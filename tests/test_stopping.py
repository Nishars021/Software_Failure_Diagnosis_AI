from src.scoring import HypothesisScore
from src.budget import InvestigationBudget
from src.stopping import should_stop


scores = [
    HypothesisScore(
        hypothesis_id="H1",
        supporting_weight=1.0,
        contradicting_weight=0.9,
        independent_evidence_count=2,
        raw_score=0.1,
        confidence=52.0
    ),
    HypothesisScore(
        hypothesis_id="H2",
        supporting_weight=1.0,
        contradicting_weight=0.9,
        independent_evidence_count=2,
        raw_score=0.1,
        confidence=49.0
    )
]


budget = InvestigationBudget()


stop, reason = should_stop(scores, budget)


print("Should stop:", stop)
print("Reason:", reason)