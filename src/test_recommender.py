from dataclasses import dataclass
from typing import List

from src.hypothesis import Hypothesis


@dataclass
class DiagnosticTest:
    description: str
    purpose: str
    expected_if_h1: str
    expected_if_h2: str


def recommend_discriminating_test(
    h1: Hypothesis,
    h2: Hypothesis
) -> DiagnosticTest:

    cause_1 = h1.cause.lower()
    cause_2 = h2.cause.lower()

    # Database vs deployment
    if (
        "database" in cause_1
        and "deployment" in cause_2
    ) or (
        "deployment" in cause_1
        and "database" in cause_2
    ):
        return DiagnosticTest(
            description=(
                "Compare database behavior between the "
                "previous and current application versions."
            ),
            purpose=(
                "Determine whether the failure is caused by "
                "the database itself or by the recent deployment."
            ),
            expected_if_h1=(
                "Database failures occur independently of the "
                "application version."
            ),
            expected_if_h2=(
                "The failure appears only with the newly deployed version."
            )
        )

    # Database vs server/resource
    if (
        "database" in cause_1
        and ("server" in cause_2 or "resource" in cause_2)
    ) or (
        "database" in cause_2
        and ("server" in cause_1 or "resource" in cause_1)
    ):
        return DiagnosticTest(
            description=(
                "Run a database health and query-latency check "
                "while monitoring server CPU and memory."
            ),
            purpose=(
                "Determine whether the bottleneck originates "
                "from the database or server resources."
            ),
            expected_if_h1=(
                "Database latency or database errors increase."
            ),
            expected_if_h2=(
                "CPU or memory becomes abnormal while database health remains normal."
            )
        )

    # Deployment vs configuration
    if (
        "deployment" in cause_1
        and "configuration" in cause_2
    ) or (
        "configuration" in cause_1
        and "deployment" in cause_2
    ):
        return DiagnosticTest(
            description=(
                "Compare the configuration and application version "
                "between the previous and current deployment."
            ),
            purpose=(
                "Determine whether the failure is associated "
                "with code changes or configuration changes."
            ),
            expected_if_h1=(
                "The failure correlates with the new application version."
            ),
            expected_if_h2=(
                "The failure correlates with a configuration difference."
            )
        )

    # Generic fallback
    return DiagnosticTest(
        description=(
            "Collect the most specific missing evidence "
            "that differs between the two hypotheses."
        ),
        purpose=(
            "Obtain evidence that can distinguish the competing hypotheses."
        ),
        expected_if_h1=(
            "The collected evidence should match the predictions of H1."
        ),
        expected_if_h2=(
            "The collected evidence should match the predictions of H2."
        )
    )