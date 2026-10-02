from src.ai_hypothesis import generate_ai_hypotheses


problem = (
    "The web application suddenly started returning "
    "HTTP 500 errors."
)


hypotheses = generate_ai_hypotheses(problem)


print("\nAI GENERATED HYPOTHESES")
print("=" * 60)

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