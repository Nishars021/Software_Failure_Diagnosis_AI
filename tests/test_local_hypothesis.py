from src.local_hypothesis import generate_local_hypotheses


problem = (
    "The web application suddenly started returning HTTP 500 errors "
    "after a new version was deployed."
)

hypotheses = generate_local_hypotheses(problem)


print("\nLOCAL AI HYPOTHESIS GENERATOR")
print("=" * 60)

print(f"\nProblem:\n{problem}")

print(f"\nGenerated hypotheses: {len(hypotheses)}")

for hypothesis in hypotheses:

    print(f"\n{hypothesis.id}: {hypothesis.cause}")

    print("Assumptions:")
    for item in hypothesis.assumptions:
        print(f"  - {item}")

    print("Predicted effects:")
    for item in hypothesis.predicted_effects:
        print(f"  - {item}")

    print("Required evidence:")
    for item in hypothesis.required_evidence:
        print(f"  - {item}")