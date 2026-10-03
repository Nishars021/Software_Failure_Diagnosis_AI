from src.hypothesis import Hypothesis
from src.scoring import HypothesisScore
from src.synthesis import combine_hypotheses


h1 = Hypothesis(
    id="H1",
    cause="Database failure",
    assumptions=["The application depends on a database"],
    predicted_effects=["Database queries fail"],
    required_evidence=["Database health check"]
)

h6 = Hypothesis(
    id="H6",
    cause="Database healthy",
    assumptions=["The database is operating normally"],
    predicted_effects=["Database queries should succeed"],
    required_evidence=["Database health check"]
)

score1 = HypothesisScore(
    hypothesis_id="H1",
    supporting_weight=0.9,
    contradicting_weight=0.0,
    independent_evidence_count=1,
    raw_score=0.9,
    confidence=90.0
)

score6 = HypothesisScore(
    hypothesis_id="H6",
    supporting_weight=0.8,
    contradicting_weight=0.0,
    independent_evidence_count=1,
    raw_score=0.8,
    confidence=80.0
)

result = combine_hypotheses(h1, h6, score1, score6)

print("INCOMPATIBLE SYNTHESIS TEST")
print("=" * 60)

if result is None:
    print("CORRECT: Incompatible hypotheses were not combined.")
else:
    print("ERROR: Incompatible hypotheses were combined.")
    print(result)