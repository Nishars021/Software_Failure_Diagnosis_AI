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

    # ==================================================
    # DATABASE HYPOTHESIS
    # ==================================================

    if "database" in cause:

        supporting_keywords = [
            "database failure",
            "database unavailable",
            "database connection",
            "connection error",
            "connection timeout",
            "query failure",
            "database error",
            "database connection timeout"
        ]

        contradicting_keywords = [
            "database healthy",
            "database is healthy",
            "database normal",
            "database operational",
            "database health check is normal",
            "database health check normal",
            "health check is normal",
            "health check normal"
        ]

        if any(word in description for word in supporting_keywords):
            return EvidenceAssessment(
                evidence=evidence,
                hypothesis_id=hypothesis.id,
                evidence_type=EvidenceType.SUPPORTING,
                explanation=(
                    "The evidence indicates a database-related failure."
                )
            )

        if any(word in description for word in contradicting_keywords):
            return EvidenceAssessment(
                evidence=evidence,
                hypothesis_id=hypothesis.id,
                evidence_type=EvidenceType.CONTRADICTING,
                explanation=(
                    "The evidence indicates that the database "
                    "is operating normally."
                )
            )

    # ==================================================
    # DEPLOYMENT HYPOTHESIS
    # ==================================================

    if "deployment" in cause:

        supporting_keywords = [
            "new deployment",
            "recent deployment",
            "deployed recently",
            "new version",
            "new version was deployed",
            "version was deployed",
            "release was deployed",
            "recent release"
        ]

        contradicting_keywords = [
            "no recent deployment",
            "no deployment",
            "no new deployment",
            "no recent release"
        ]

        if any(word in description for word in supporting_keywords):
            return EvidenceAssessment(
                evidence=evidence,
                hypothesis_id=hypothesis.id,
                evidence_type=EvidenceType.SUPPORTING,
                explanation=(
                    "The evidence indicates that a recent "
                    "deployment occurred."
                )
            )

        if any(word in description for word in contradicting_keywords):
            return EvidenceAssessment(
                evidence=evidence,
                hypothesis_id=hypothesis.id,
                evidence_type=EvidenceType.CONTRADICTING,
                explanation=(
                    "The evidence indicates that no recent "
                    "deployment occurred."
                )
            )

    # ==================================================
    # SERVER / RESOURCE HYPOTHESIS
    # ==================================================

    if "server" in cause or "resource" in cause:

        supporting_keywords = [
            "high cpu",
            "cpu is high",
            "cpu usage is extremely high",
            "cpu usage high",
            "high cpu usage",
            "high memory",
            "memory is high",
            "memory usage high",
            "memory usage is extremely high",
            "high memory usage",
            "resource exhausted",
            "resource exhaustion",
            "server resource exhaustion"
        ]

        contradicting_keywords = [
            "cpu normal",
            "cpu is normal",
            "cpu usage is normal",
            "memory normal",
            "memory is normal",
            "memory usage is normal",
            "resources normal",
            "server resources are normal"
        ]

        if any(word in description for word in supporting_keywords):
            return EvidenceAssessment(
                evidence=evidence,
                hypothesis_id=hypothesis.id,
                evidence_type=EvidenceType.SUPPORTING,
                explanation=(
                    "The evidence indicates that server resources "
                    "may be under pressure."
                )
            )

        if any(word in description for word in contradicting_keywords):
            return EvidenceAssessment(
                evidence=evidence,
                hypothesis_id=hypothesis.id,
                evidence_type=EvidenceType.CONTRADICTING,
                explanation=(
                    "The evidence indicates that server resources "
                    "are operating normally."
                )
            )

    # ==================================================
    # EXTERNAL API HYPOTHESIS
    # ==================================================

    if "external api" in cause:

        supporting_keywords = [
            "api failure",
            "api unavailable",
            "api timeout",
            "api health check failed",
            "external api health check failed",
            "external api failure",
            "external api unavailable",
            "external service failure",
            "external service unavailable"
        ]

        contradicting_keywords = [
            "api healthy",
            "api is healthy",
            "api normal",
            "api health check is normal",
            "api health check normal",
            "external api is healthy",
            "external service healthy",
            "external service is healthy"
        ]

        if any(word in description for word in supporting_keywords):
            return EvidenceAssessment(
                evidence=evidence,
                hypothesis_id=hypothesis.id,
                evidence_type=EvidenceType.SUPPORTING,
                explanation=(
                    "The evidence indicates that an external "
                    "API may be failing."
                )
            )

        if any(word in description for word in contradicting_keywords):
            return EvidenceAssessment(
                evidence=evidence,
                hypothesis_id=hypothesis.id,
                evidence_type=EvidenceType.CONTRADICTING,
                explanation=(
                    "The evidence indicates that the external "
                    "API is operating normally."
                )
            )

    # ==================================================
    # CONFIGURATION HYPOTHESIS
    # ==================================================

    if "configuration" in cause or "environment" in cause:

        supporting_keywords = [
            "configuration error",
            "configuration changed",
            "config changed",
            "incorrect configuration",
            "environment configuration is incorrect",
            "environment configuration incorrect",
            "incorrect environment configuration",
            "environment variable changed",
            "environment variable is incorrect",
            "wrong configuration",
            "configuration is incorrect"
        ]

        contradicting_keywords = [
            "configuration is correct",
            "configuration is normal",
            "environment configuration is correct",
            "environment configuration is normal"
        ]

        if any(word in description for word in supporting_keywords):
            return EvidenceAssessment(
                evidence=evidence,
                hypothesis_id=hypothesis.id,
                evidence_type=EvidenceType.SUPPORTING,
                explanation=(
                    "The evidence indicates a possible "
                    "configuration problem."
                )
            )

        if any(word in description for word in contradicting_keywords):
            return EvidenceAssessment(
                evidence=evidence,
                hypothesis_id=hypothesis.id,
                evidence_type=EvidenceType.CONTRADICTING,
                explanation=(
                    "The evidence indicates that the configuration "
                    "is operating normally."
                )
            )

    # ==================================================
    # NO CLEAR RELATIONSHIP
    # ==================================================

    return EvidenceAssessment(
        evidence=evidence,
        hypothesis_id=hypothesis.id,
        evidence_type=EvidenceType.MISSING,
        explanation=(
            "The available evidence does not provide enough "
            "information to evaluate this hypothesis."
        )
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