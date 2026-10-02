from hypothesis import Hypothesis


def generate_hypotheses(problem: str):
    """
    Generate an initial set of competing hypotheses
    for a software failure.
    """

    hypotheses = [
        Hypothesis(
            id="H1",
            cause="Database failure",
            assumptions=[
                "The application depends on a database",
                "The database may be unavailable or malfunctioning"
            ],
            predicted_effects=[
                "Database connection errors",
                "Database query failures",
                "HTTP 500 responses"
            ],
            required_evidence=[
                "Database health status",
                "Database logs",
                "Database connection errors"
            ]
        ),

        Hypothesis(
            id="H2",
            cause="Recent software deployment",
            assumptions=[
                "A new version was deployed recently",
                "The deployment may contain a defect"
            ],
            predicted_effects=[
                "Failures begin after deployment",
                "Errors appear in the newly deployed version"
            ],
            required_evidence=[
                "Deployment history",
                "Application version information",
                "Logs before and after deployment"
            ]
        ),

        Hypothesis(
            id="H3",
            cause="Server or resource problem",
            assumptions=[
                "The application depends on sufficient server resources",
                "CPU, memory, or other resources may be exhausted"
            ],
            predicted_effects=[
                "High CPU or memory usage",
                "Slow application response",
                "Application failures"
            ],
            required_evidence=[
                "CPU usage",
                "Memory usage",
                "Server monitoring logs"
            ]
        ),

        Hypothesis(
            id="H4",
            cause="External API failure",
            assumptions=[
                "The application depends on an external service",
                "The external service may be unavailable or slow"
            ],
            predicted_effects=[
                "API timeout errors",
                "Failed external requests",
                "Application failures"
            ],
            required_evidence=[
                "API response status",
                "API latency",
                "External service logs"
            ]
        ),

        Hypothesis(
            id="H5",
            cause="Configuration or environment problem",
            assumptions=[
                "The application depends on environment configuration",
                "A configuration value may be incorrect"
            ],
            predicted_effects=[
                "Configuration-related errors",
                "Application startup or runtime failures"
            ],
            required_evidence=[
                "Environment configuration",
                "Configuration change history",
                "Application error logs"
            ]
        ),

        Hypothesis(
            id="UNKNOWN",
            cause="Insufficient evidence to determine the cause"
        )
    ]

    return hypotheses