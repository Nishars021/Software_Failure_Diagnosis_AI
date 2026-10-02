from src.hypothesis import Hypothesis
from src.evidence import Evidence, assess_evidence
from src.scoring import (
    calculate_hypothesis_score,
    update_hypothesis_score
)


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


# Initial evidence
evidence_1 = Evidence(
    id="E1",
    description="Database connection timeout detected",
    source="Application logs",
    source_id="APP_LOG_001",
    reliability=0.90
)


assessment_1 = assess_evidence(
    hypothesis,
    evidence_1
)


initial_score = calculate_hypothesis_score(
    hypothesis_id="H1",
    assessments=[assessment_1]
)


print("INITIAL")
print("Confidence:", round(initial_score.confidence, 2), "%")


# New evidence arrives
evidence_2 = Evidence(
    id="E2",
    description="Database health check is normal",
    source="Independent health monitor",
    source_id="DB_HEALTH_001",
    reliability=0.70
)


assessment_2 = assess_evidence(
    hypothesis,
    evidence_2
)


updated_score = update_hypothesis_score(
    previous_score=initial_score,
    new_assessment=assessment_2
)


print("\nAFTER NEW EVIDENCE")
print("Confidence:", round(updated_score.confidence, 2), "%")
print("Supporting:", updated_score.supporting_weight)
print("Contradicting:", updated_score.contradicting_weight)