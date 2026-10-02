from src.hypothesis import Hypothesis


def generate_local_hypotheses(problem: str):
    """
    Local hypothesis generator.
    Works without an internet connection or API credits.

    It detects clues in the failure description and generates
    multiple possible software failure hypotheses.
    """

    problem_lower = problem.lower()

    hypotheses = []

    # ---------------------------------------------------------
    # H1 - Database failure
    # ---------------------------------------------------------
    if any(keyword in problem_lower for keyword in [
        "database",
        "db",
        "sql",
        "query",
        "connection timeout",
        "connection error"
    ]):
        hypotheses.append(
            Hypothesis(
                id="H1",
                cause="Database failure",
                assumptions=[
                    "The application depends on a database",
                    "The database may be unavailable or returning errors"
                ],
                predicted_effects=[
                    "Database queries fail",
                    "Application requests may return HTTP 500 errors"
                ],
                required_evidence=[
                    "Database health check",
                    "Database connection logs",
                    "Query or database error logs"
                ]
            )
        )

    # ---------------------------------------------------------
    # H2 - Recent deployment
    # ---------------------------------------------------------
    if any(keyword in problem_lower for keyword in [
        "deployment",
        "deployed",
        "deploy",
        "new version",
        "release",
        "after update",
        "after upgrade"
    ]):
        hypotheses.append(
            Hypothesis(
                id="H2",
                cause="Recent software deployment",
                assumptions=[
                    "A new version was recently released",
                    "The failure started after the deployment"
                ],
                predicted_effects=[
                    "Errors appear after the new version is deployed",
                    "Rolling back the deployment may remove the failure"
                ],
                required_evidence=[
                    "Deployment history",
                    "Application version information",
                    "Changes introduced in the latest release"
                ]
            )
        )

    # ---------------------------------------------------------
    # H3 - Server/resource problem
    # ---------------------------------------------------------
    if any(keyword in problem_lower for keyword in [
        "server",
        "cpu",
        "memory",
        "ram",
        "resource",
        "disk",
        "overloaded",
        "high traffic",
        "capacity"
    ]):
        hypotheses.append(
            Hypothesis(
                id="H3",
                cause="Server/resource problem",
                assumptions=[
                    "The application is running on a server",
                    "The server may have insufficient or exhausted resources"
                ],
                predicted_effects=[
                    "CPU or memory usage may become unusually high",
                    "Requests may fail or become slow"
                ],
                required_evidence=[
                    "CPU utilization",
                    "Memory utilization",
                    "Server resource monitoring logs"
                ]
            )
        )

    # ---------------------------------------------------------
    # H4 - External API failure
    # ---------------------------------------------------------
    if any(keyword in problem_lower for keyword in [
        "api",
        "external service",
        "third-party",
        "third party",
        "external service",
        "service unavailable"
    ]):
        hypotheses.append(
            Hypothesis(
                id="H4",
                cause="External API failure",
                assumptions=[
                    "The application depends on an external service",
                    "The external service may be unavailable or timing out"
                ],
                predicted_effects=[
                    "API requests fail or time out",
                    "Application requests depending on the API may return errors"
                ],
                required_evidence=[
                    "External API health status",
                    "API response logs",
                    "API timeout or connection errors"
                ]
            )
        )

    # ---------------------------------------------------------
    # H5 - Configuration/environment problem
    # ---------------------------------------------------------
    if any(keyword in problem_lower for keyword in [
        "configuration",
        "config",
        "environment",
        "environment variable",
        "env variable",
        "settings"
    ]):
        hypotheses.append(
            Hypothesis(
                id="H5",
                cause="Configuration/environment problem",
                assumptions=[
                    "The application depends on environment configuration",
                    "A configuration value may be incorrect or changed"
                ],
                predicted_effects=[
                    "The application may fail during startup or execution",
                    "Configuration-dependent operations may fail"
                ],
                required_evidence=[
                    "Configuration files",
                    "Environment variables",
                    "Recent configuration changes"
                ]
            )
        )

    # ---------------------------------------------------------
    # Add general hypotheses when clues are insufficient
    # ---------------------------------------------------------
    general_hypotheses = [
        Hypothesis(
            id="H1",
            cause="Database failure",
            assumptions=[
                "The application may depend on a database"
            ],
            predicted_effects=[
                "Database operations may fail",
                "Application requests may return errors"
            ],
            required_evidence=[
                "Database health check",
                "Database logs"
            ]
        ),
        Hypothesis(
            id="H2",
            cause="Recent software deployment",
            assumptions=[
                "A recent software change may have introduced the failure"
            ],
            predicted_effects=[
                "Errors may begin after a new release"
            ],
            required_evidence=[
                "Deployment history",
                "Application version"
            ]
        ),
        Hypothesis(
            id="H3",
            cause="Server/resource problem",
            assumptions=[
                "The application may be affected by server resources"
            ],
            predicted_effects=[
                "High resource usage may cause request failures"
            ],
            required_evidence=[
                "CPU and memory metrics"
            ]
        ),
        Hypothesis(
            id="H4",
            cause="External API failure",
            assumptions=[
                "The application may depend on an external service"
            ],
            predicted_effects=[
                "External requests may fail"
            ],
            required_evidence=[
                "API health status",
                "API logs"
            ]
        ),
        Hypothesis(
            id="H5",
            cause="Configuration/environment problem",
            assumptions=[
                "The application may depend on configuration values"
            ],
            predicted_effects=[
                "Incorrect configuration may cause application failures"
            ],
            required_evidence=[
                "Configuration values",
                "Environment variables"
            ]
        )
    ]

    # If fewer than 3 hypotheses were detected,
    # add general alternatives.
    if len(hypotheses) < 3:

        existing_causes = {
            hypothesis.cause
            for hypothesis in hypotheses
        }

        for hypothesis in general_hypotheses:

            if hypothesis.cause not in existing_causes:
                hypotheses.append(hypothesis)

            if len(hypotheses) >= 5:
                break

    # ---------------------------------------------------------
    # UNKNOWN hypothesis
    # ---------------------------------------------------------
    hypotheses.append(
        Hypothesis(
            id="UNKNOWN",
            cause="Insufficient evidence to determine the cause",
            assumptions=[
                "Available information may not identify the actual failure"
            ],
            predicted_effects=[
                "Additional investigation is required"
            ],
            required_evidence=[
                "Additional diagnostic evidence"
            ]
        )
    )

    # Reassign IDs safely
    known_hypotheses = [
        hypothesis
        for hypothesis in hypotheses
        if hypothesis.id != "UNKNOWN"
    ]

    for index, hypothesis in enumerate(known_hypotheses, start=1):
        hypothesis.id = f"H{index}"

    return known_hypotheses + [
        hypothesis for hypothesis in hypotheses
        if hypothesis.id == "UNKNOWN"
    ]