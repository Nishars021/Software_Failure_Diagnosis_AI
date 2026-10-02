from src.scoring import HypothesisScore
from src.decision import make_decision


scores = [

    HypothesisScore(
        hypothesis_id="H1",
        supporting_weight=0.0,
        contradicting_weight=0.8,
        independent_evidence_count=1,
        raw_score=-0.8,
        confidence=10
    ),

    HypothesisScore(
        hypothesis_id="H2",
        supporting_weight=0.0,
        contradicting_weight=0.8,
        independent_evidence_count=1,
        raw_score=-0.8,
        confidence=10
    ),

    HypothesisScore(
        hypothesis_id="H3",
        supporting_weight=0.0,
        contradicting_weight=0.7,
        independent_evidence_count=1,
        raw_score=-0.7,
        confidence=12
    ),

    HypothesisScore(
        hypothesis_id="H4",
        supporting_weight=0.0,
        contradicting_weight=0.8,
        independent_evidence_count=1,
        raw_score=-0.8,
        confidence=10
    ),

    HypothesisScore(
        hypothesis_id="H5",
        supporting_weight=0.0,
        contradicting_weight=0.7,
        independent_evidence_count=1,
        raw_score=-0.7,
        confidence=12
    )
]


decision = make_decision(scores)

print("Outcome:", decision.outcome)
print("Selected:", decision.selected_hypotheses)
print("Explanation:", decision.explanation)