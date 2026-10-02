from src.hypothesis import Hypothesis
from src.test_recommender import recommend_discriminating_test


h1 = Hypothesis(
    id="H1",
    cause="Database failure",
    assumptions=[
        "The application depends on a database"
    ],
    predicted_effects=[
        "Database connection errors",
        "Database query failures"
    ],
    required_evidence=[
        "Database health status",
        "Database logs"
    ]
)


h2 = Hypothesis(
    id="H2",
    cause="Recent software deployment",
    assumptions=[
        "A new version was deployed recently"
    ],
    predicted_effects=[
        "Failures begin after deployment"
    ],
    required_evidence=[
        "Deployment history",
        "Application version information"
    ]
)


test = recommend_discriminating_test(h1, h2)


print("RECOMMENDED TEST")
print("----------------")
print("Test:", test.description)
print()
print("Purpose:", test.purpose)
print()
print("If H1 is true:")
print(test.expected_if_h1)
print()
print("If H2 is true:")
print(test.expected_if_h2)