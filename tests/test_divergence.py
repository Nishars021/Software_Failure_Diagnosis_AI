from src.divergence import generate_hypotheses


problem = "The web application suddenly started returning HTTP 500 errors."

hypotheses = generate_hypotheses(problem)

for hypothesis in hypotheses:
    print("\n--------------------")
    print(hypothesis.id)
    print("Cause:", hypothesis.cause)
    print("Assumptions:", hypothesis.assumptions)
    print("Predicted effects:", hypothesis.predicted_effects)
    print("Required evidence:", hypothesis.required_evidence)