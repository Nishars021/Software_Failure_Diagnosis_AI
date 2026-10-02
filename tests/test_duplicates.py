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


result = calculate_distinctness(h1, h2)

print("Distinctness result:")
print(result)