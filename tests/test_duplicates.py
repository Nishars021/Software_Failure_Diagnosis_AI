from src.hypothesis import Hypothesis
from src.evidence import Evidence, EvidenceType, EvidenceAssessment
from src.scoring import calculate_hypothesis_score


hypothesis = Hypothesis(
    id="H1",
    cause="Database failure"
)


evidence1 = Evidence(
    id="E1",
    description="Database connection timeout detected",
    source="Application logs",
    source_id="LOG001",
    reliability=0.9
)


evidence2 = Evidence(
    id="E2",
    description="Database connection timeout detected again",
    source="Application logs",
    source_id="LOG001",
    reliability=0.9
)


assessment1 = EvidenceAssessment(
    evidence=evidence1,
    hypothesis_id="H1",
    evidence_type=EvidenceType.SUPPORTING,
    explanation="Supports database failure"
)


assessment2 = EvidenceAssessment(
    evidence=evidence2,
    hypothesis_id="H1",
    evidence_type=EvidenceType.SUPPORTING,
    explanation="Same source as E1"
)


score = calculate_hypothesis_score(
    "H1",
    [assessment1, assessment2]
)


print("Independent evidence count:", score.independent_evidence_count)
print("Supporting weight:", score.supporting_weight)

assert score.independent_evidence_count == 1

print("Duplicate evidence test PASSED")