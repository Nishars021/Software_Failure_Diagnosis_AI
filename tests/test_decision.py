from src.scoring import HypothesisScore
from src.decision import make_decision


scores = [
    HypothesisScore(
        hypothesis_id="H1",
        supporting_weight=0.4,
        contradicting_weight=0.6,
        independent_evidence_count=2,
        raw_score=-0.2,
        confidence=40.0
    ),

    HypothesisScore(
        hypothesis_id="H2",
        supporting_weight=0.3,
        contradicting_weight=0.7,
        independent_evidence_count=2,
        raw_score=-0.4,
        confidence=30.0
    )
]


decision = make_decision(scores)


print("Outcome:", decision.outcome)
print("Selected:", decision.selected_hypotheses)
print("Explanation:", decision.explanation)