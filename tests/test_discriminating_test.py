from src.hypothesis import Hypothesis
from src.test_recommender import recommend_discriminating_test


h1 = Hypothesis(
    id="H1",
    cause="Database failure",
    assumptions=["The application depends on a database"],
    predicted_effects=["Database queries fail"],
    required_evidence=["Database health check"]
)

h2 = Hypothesis(
    id="H2",
    cause="Recent software deployment",
    assumptions=["A new version was recently deployed"],
    predicted_effects=["Errors appeared after deployment"],
    required_evidence=["Deployment history"]
)


result = recommend_discriminating_test(h1, h2)

print("DISCRIMINATING TEST")
print("=" * 60)

if result:
    print("TEST RECOMMENDED")
    print()
    print("Description:", result.description)
    print("Purpose:", result.purpose)
    print("Expected if H1:", result.expected_if_h1)
    print("Expected if H2:", result.expected_if_h2)
else:
    print("ERROR: No discriminating test was generated.")