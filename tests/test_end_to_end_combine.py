from src.main import diagnose
from src.evidence import Evidence


def test_end_to_end_combine():

    problem = (
        "The web application started returning HTTP 500 errors "
        "after a recent software change."
    )

    evidence_list = [
        Evidence(
            id="E1",
            description="Database connection timeout detected",
            source="Application logs",
            source_id="LOG001",
            reliability=0.9
        ),
        Evidence(
            id="E2",
            description="A new version was recently deployed",
            source="Deployment system",
            source_id="DEP001",
            reliability=0.9
        )
    ]

    result = diagnose(problem, evidence_list)

    print("\nEND-TO-END COMBINE TEST")
    print("=" * 60)
    print("Outcome:", result["decision"].outcome)
    print("Selected:", result["decision"].selected_hypotheses)
    print("Explanation:", result["decision"].explanation)

    assert result["decision"].outcome == "COMBINE"
    assert result["decision"].selected_hypotheses == ["H1", "H2"]