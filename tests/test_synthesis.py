from src.hypothesis import Hypothesis
from src.scoring import HypothesisScore
from src.synthesis import combine_hypotheses


h1 = Hypothesis(
    id="H1",
    cause="Database failure",
    assumptions=[
        "The application depends on a database"
    ],
    predicted_effects=[
        "Database queries fail"
    ],
    required_evidence=[
        "Database health check"
    ]
)

h2 = Hypothesis(
    id="H2",
    cause="Recent software deployment",
    assumptions=[
        "A new version was recently deployed"
    ],
    predicted_effects=[
        "Errors appeared after deployment"
    ],
    required_evidence=[
        "Deployment history"
    ]
)


score1 = HypothesisScore(
    hypothesis_id="H1",
    supporting_weight=0.9,
    contradicting_weight=0.0,
    independent_evidence_count=1,
    raw_score=0.9,
    confidence=90.0
)

score2 = HypothesisScore(
    hypothesis_id="H2",
    supporting_weight=0.8,
    contradicting_weight=0.0,
    independent_evidence_count=1,
    raw_score=0.8,
    confidence=80.0
)


combined = combine_hypotheses(
    h1,
    h2,
    score1,
    score2
)


print("\nSYNTHESIS TEST")
print("=" * 60)


if combined is None:
    print("COMBINE FAILED")
else:
    print("COMBINE SUCCESSFUL")

    print(f"\nID: {combined.id}")
    print(f"Cause: {combined.cause}")

    print("\nAssumptions:")
    for item in combined.assumptions:
        print(f"  - {item}")

    print("\nPredicted effects:")
    for item in combined.predicted_effects:
        print(f"  - {item}")

    print("\nRequired evidence:")
    for item in combined.required_evidence:
        print(f"  - {item}")