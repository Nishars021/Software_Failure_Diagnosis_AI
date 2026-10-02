from src.hypothesis import Hypothesis
from src.evidence import Evidence, assess_evidence
from src.scoring import calculate_hypothesis_score


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


evidence_1 = Evidence(
    id="E1",
    description="Database connection timeout detected",
    source="Application logs",
    source_id="APP_LOG_001",
    reliability=0.90
)


evidence_2 = Evidence(
    id="E2",
    description="Database query failure detected",
    source="Database monitoring",
    source_id="DB_MONITOR_001",
    reliability=0.80
)


evidence_3 = Evidence(
    id="E3",
    description="Database health check is normal",
    source="Independent health monitor",
    source_id="DB_HEALTH_001",
    reliability=0.70
)


assessment_1 = assess_evidence(hypothesis, evidence_1)
assessment_2 = assess_evidence(hypothesis, evidence_2)
assessment_3 = assess_evidence(hypothesis, evidence_3)


assessments = [
    assessment_1,
    assessment_2,
    assessment_3
]


result = calculate_hypothesis_score(
    hypothesis_id="H1",
    assessments=assessments
)


print("Hypothesis:", result.hypothesis_id)
print("Supporting weight:", result.supporting_weight)
print("Contradicting weight:", result.contradicting_weight)
print("Independent evidence:", result.independent_evidence_count)
print("Raw score:", result.raw_score)
print("Confidence:", round(result.confidence, 2), "%")