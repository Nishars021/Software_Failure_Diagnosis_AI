from src.hypothesis import Hypothesis
from src.scoring import HypothesisScore
from src.decision import synthesize_hypotheses


h1 = Hypothesis(
    id="H1",
    cause="Database failure",
    assumptions=[
        "Application depends on database"
    ],
    predicted_effects=[
        "Database latency increases"
    ],
    required_evidence=[
        "Database monitoring"
    ]
)


h2 = Hypothesis(
    id="H2",
    cause="Server resource problem",
    assumptions=[
        "Application requires sufficient server resources"
    ],
    predicted_effects=[
        "Memory or CPU usage increases"
    ],
    required_evidence=[
        "Server monitoring"
    ]
)


score1 = HypothesisScore(
    hypothesis_id="H1",
    supporting_weight=0.9,
    contradicting_weight=0.1,
    independent_evidence_count=2,
    raw_score=0.8,
    confidence=80.0
)


score2 = HypothesisScore(
    hypothesis_id="H2",
    supporting_weight=0.8,
    contradicting_weight=0.1,
    independent_evidence_count=2,
    raw_score=0.7,
    confidence=77.78
)


decision = synthesize_hypotheses(
    h1,
    h2,
    score1,
    score2
)


print("Outcome:", decision.outcome)
print("Hypotheses:", decision.selected_hypotheses)
print("Explanation:", decision.explanation)