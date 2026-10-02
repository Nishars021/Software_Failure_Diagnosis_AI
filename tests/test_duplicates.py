from src.hypothesis import Hypothesis
from src.distinctness import calculate_distinctness


h1 = Hypothesis(
    id="H1",
    cause="Database failure",
    assumptions=[
        "Application depends on database"
    ],
    predicted_effects=[
        "Database connection errors"
    ],
    required_evidence=[
        "Database logs"
    ]
)


h2 = Hypothesis(
    id="H2",
    cause="Recent software deployment",
    assumptions=[
        "A new version was deployed recently",
        "The deployment may contain a defect"
    ],
    predicted_effects=[
        "Failures begin after deployment",
        "Errors appear in the new version"
    ],
    required_evidence=[
        "Deployment history",
        "Application version information"
    ]
)


result = calculate_distinctness(h1, h2)

print("Distinctness result:")
print(result)