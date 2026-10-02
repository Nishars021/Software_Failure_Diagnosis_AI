from src.hypothesis import Hypothesis
from src.evidence import Evidence, assess_evidence


hypothesis = Hypothesis(
    id="H1",
    cause="Database failure",
    assumptions=[
        "The application depends on a database"
    ],
    predicted_effects=[
        "Database connection errors"
    ],
    required_evidence=[
        "Database logs"
    ]
)


evidence = Evidence(
    id="E1",
    description="Database health check is normal",
    source="Application logs",
    source_id="APP_LOG_001",
    reliability=0.95
)


result = assess_evidence(hypothesis, evidence)


print("Hypothesis:", result.hypothesis_id)
print("Evidence:", result.evidence.description)
print("Classification:", result.evidence_type.value)
print("Explanation:", result.explanation)