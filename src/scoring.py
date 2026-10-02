from dataclasses import dataclass
from typing import List

from src.evidence import EvidenceAssessment, EvidenceType


@dataclass
class HypothesisScore:
    hypothesis_id: str
    supporting_weight: float
    contradicting_weight: float
    independent_evidence_count: int
    raw_score: float
    confidence: float


def calculate_hypothesis_score(
    hypothesis_id: str,
    assessments: List[EvidenceAssessment]
) -> HypothesisScore:

    supporting_weight = 0.0
    contradicting_weight = 0.0
    independent_evidence_count = 0

    # Keep track of sources already counted
    counted_sources = set()

    for assessment in assessments:

        evidence = assessment.evidence
        source_id = evidence.source_id

        # Dependent evidence should not be counted
        # as another independent confirmation.
        if assessment.evidence_type == EvidenceType.DEPENDENT:
            continue

        # Don't count the same source twice.
        if source_id in counted_sources:
            continue

        counted_sources.add(source_id)
        independent_evidence_count += 1

        if assessment.evidence_type == EvidenceType.SUPPORTING:
            supporting_weight += evidence.reliability

        elif assessment.evidence_type == EvidenceType.CONTRADICTING:
            contradicting_weight += evidence.reliability

    total_weight = supporting_weight + contradicting_weight

    # No usable evidence means we cannot calculate
    # a meaningful confidence.
    if total_weight == 0:
        confidence = 0.0
        raw_score = 0.0

    else:
        raw_score = supporting_weight - contradicting_weight

        confidence = (
            (raw_score + total_weight)
            / (2 * total_weight)
        ) * 100

    return HypothesisScore(
        hypothesis_id=hypothesis_id,
        supporting_weight=supporting_weight,
        contradicting_weight=contradicting_weight,
        independent_evidence_count=independent_evidence_count,
        raw_score=raw_score,
        confidence=confidence
    )