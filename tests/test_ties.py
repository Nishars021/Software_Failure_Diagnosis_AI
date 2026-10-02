from src.scoring import HypothesisScore
from src.decision import make_decision


scores = [

    HypothesisScore(
        hypothesis_id="H1",
        supporting_weight=0.8,
        contradicting_weight=0.1,
        independent_evidence_count=2,
        raw_score=0.7,
        confidence=52
    ),

    HypothesisScore(
        hypothesis_id="H2",
        supporting_weight=0.8,
        contradicting_weight=0.2,
        independent_evidence_count=2,
        raw_score=0.6,
        confidence=49
    )
]


decision = make_decision(scores)

print("Outcome:", decision.outcome)
print("Selected:", decision.selected_hypotheses)
print("Explanation:", decision.explanation)

assert decision.outcome == "TEST"

print("Tie test PASSED")