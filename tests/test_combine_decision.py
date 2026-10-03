from src.hypothesis import Hypothesis
from src.scoring import HypothesisScore
from src.decision import make_decision


def test_combine_decision():

    h1 = Hypothesis(
        id="H1",
        cause="Database failure",
        assumptions=["Application depends on database"],
        predicted_effects=["Database queries fail"],
        required_evidence=["Database health check"]
    )

    h2 = Hypothesis(
        id="H2",
        cause="Recent software deployment",
        assumptions=["New version was recently deployed"],
        predicted_effects=["Errors appeared after deployment"],
        required_evidence=["Deployment history"]
    )

    scores = [
        HypothesisScore(
            hypothesis_id="H1",
            supporting_weight=0.7,
            contradicting_weight=0.0,
            independent_evidence_count=1,
            raw_score=0.7,
            confidence=70.0
        ),
        HypothesisScore(
            hypothesis_id="H2",
            supporting_weight=0.65,
            contradicting_weight=0.0,
            independent_evidence_count=1,
            raw_score=0.65,
            confidence=65.0
        )
    ]

    hypotheses = [h1, h2]

    decision = make_decision(scores, hypotheses)

    print("\nCOMBINE DECISION TEST")
    print("=" * 60)
    print("Outcome:", decision.outcome)
    print("Selected:", decision.selected_hypotheses)
    print("Explanation:", decision.explanation)

    assert decision.outcome == "COMBINE"
    assert decision.selected_hypotheses == ["H1", "H2"]