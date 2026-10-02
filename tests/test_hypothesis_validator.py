from src.local_hypothesis import generate_local_hypotheses
from src.hypothesis_validator import validate_hypotheses


problem = (
    "The web application suddenly started returning HTTP 500 errors "
    "after a new version was deployed."
)


print("\nHYPOTHESIS VALIDATION TEST")
print("=" * 60)


# Generate hypotheses
hypotheses = generate_local_hypotheses(problem)

print(f"\nGenerated: {len(hypotheses)} hypotheses")


# Validate hypotheses
validated = validate_hypotheses(hypotheses)

print(f"After validation: {len(validated)} hypotheses")


print("\nVALIDATED HYPOTHESES")
print("-" * 60)


for hypothesis in validated:

    print(f"{hypothesis.id}: {hypothesis.cause}")


print("\nValidation completed successfully.")