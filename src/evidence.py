from dataclasses import dataclass
from enum import Enum

from src.hypothesis import Hypothesis

@dataclass
class Evidence:
    id: str
    description: str
    source: str
    source_id: str
    reliability: float = 1.0



class EvidenceType(Enum):
    SUPPORTING = "supporting"
    CONTRADICTING = "contradicting"
    MISSING = "missing"
    DEPENDENT = "dependent"

@dataclass
class EvidenceAssessment:
    evidence: Evidence
    hypothesis_id: str
    evidence_type: EvidenceType
    explanation: str




def assess_evidence(
    hypothesis: Hypothesis,
    evidence: Evidence
) -> EvidenceAssessment:

    description = evidence.description.lower()
    cause = hypothesis.cause.lower()

    # Database hypothesis
    if "database" in cause:

        if any(word in description for word in [
            "database failure",
            "database unavailable",
            "connection error",
            "connection timeout",
            "query failure",
            "database error"
        ]):
            return EvidenceAssessment(
                evidence=evidence,
                hypothesis_id=hypothesis.id,
                evidence_type=EvidenceType.SUPPORTING,
                explanation="The evidence indicates a database-related failure."
            )

        if any(word in description for word in [
            "database healthy",
            "database is healthy",
            "database normal",
            "database operational",
            "database health check is normal",
            "database health check normal",
            "health check is normal",
            "health check normal"
        ]):
            return EvidenceAssessment(
                evidence=evidence,
                hypothesis_id=hypothesis.id,
                evidence_type=EvidenceType.CONTRADICTING,
                explanation="The evidence indicates that the database is operating normally."
            )

    # Deployment hypothesis
    if "deployment" in cause:

        if any(word in description for word in [
            "new deployment",
            "recent deployment",
            "deployed recently",
            "new version"
        ]):
            return EvidenceAssessment(
                evidence=evidence,
                hypothesis_id=hypothesis.id,
                evidence_type=EvidenceType.SUPPORTING,
                explanation="The evidence indicates that a recent deployment occurred."
            )

        if any(word in description for word in [
            "no recent deployment",
            "no deployment"
        ]):
            return EvidenceAssessment(
                evidence=evidence,
                hypothesis_id=hypothesis.id,
                evidence_type=EvidenceType.CONTRADICTING,
                explanation="The evidence indicates that no recent deployment occurred."
            )

    # Server/resource hypothesis
    if "server" in cause or "resource" in cause:

        if any(word in description for word in [
            "high cpu",
            "cpu is high",
            "high memory",
            "memory usage high",
            "resource exhausted",
            "resource exhaustion"
        ]):
            return EvidenceAssessment(
                evidence=evidence,
                hypothesis_id=hypothesis.id,
                evidence_type=EvidenceType.SUPPORTING,
                explanation="The evidence indicates that server resources may be under pressure."
            )

        if any(word in description for word in [
            "cpu normal",
            "cpu is normal",
            "memory normal",
            "resources normal"
        ]):
            return EvidenceAssessment(
                evidence=evidence,
                hypothesis_id=hypothesis.id,
                evidence_type=EvidenceType.CONTRADICTING,
                explanation="The evidence indicates that server resources are operating normally."
            )

    # External API hypothesis
    if "external api" in cause:

        if any(word in description for word in [
            "api failure",
            "api unavailable",
            "api timeout",
            "external service failure"
        ]):
            return EvidenceAssessment(
                evidence=evidence,
                hypothesis_id=hypothesis.id,
                evidence_type=EvidenceType.SUPPORTING,
                explanation="The evidence indicates that an external API may be failing."
            )

        if any(word in description for word in [
            "api healthy",
            "api is healthy",
            "api normal",
            "external service healthy"
        ]):
            return EvidenceAssessment(
                evidence=evidence,
                hypothesis_id=hypothesis.id,
                evidence_type=EvidenceType.CONTRADICTING,
                explanation="The evidence indicates that the external API is operating normally."
            )

    # Configuration hypothesis
    if "configuration" in cause:

        if any(word in description for word in [
            "configuration error",
            "configuration changed",
            "config changed",
            "environment variable changed",
            "incorrect configuration"
        ]):
            return EvidenceAssessment(
                evidence=evidence,
                hypothesis_id=hypothesis.id,
                evidence_type=EvidenceType.SUPPORTING,
                explanation="The evidence indicates a possible configuration problem."
            )

    # No clear relationship found
    return EvidenceAssessment(
        evidence=evidence,
        hypothesis_id=hypothesis.id,
        evidence_type=EvidenceType.MISSING,
        explanation="The available evidence does not provide enough information to evaluate this hypothesis."
    )

def check_evidence_dependency(
    evidence_1: Evidence,
    evidence_2: Evidence
) -> bool:
    """
    Check whether two evidence items come from
    the same original source.

    Returns:
        True  -> evidence is dependent
        False -> evidence is potentially independent
    """

    return evidence_1.source_id == evidence_2.source_id