from src.hypothesis import Hypothesis
from src.divergence import generate_hypotheses
from src.distinctness import calculate_distinctness
from src.scoring import HypothesisScore
from src.decision import make_decision
from src.synthesis import combine_hypotheses
from src.test_recommender import recommend_discriminating_test
from src.budget import InvestigationBudget
from src.stopping import should_stop


def test_divergence_generates_multiple_hypotheses():
    problem = "The web application suddenly started returning HTTP 500 errors."

    hypotheses = generate_hypotheses(problem)

    assert len(hypotheses) >= 3

    ids = [h.id for h in hypotheses]

    assert "UNKNOWN" in ids


def test_hypotheses_are_distinct():
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

    result = calculate_distinctness(h1, h2)

    assert result["overall_score"] > 0


def test_decision_selects_strong_hypothesis():
    scores = [
        HypothesisScore(
            hypothesis_id="H1",
            supporting_weight=0.9,
            contradicting_weight=0.0,
            independent_evidence_count=2,
            raw_score=0.9,
            confidence=90.0
        ),
        HypothesisScore(
            hypothesis_id="H2",
            supporting_weight=0.2,
            contradicting_weight=0.0,
            independent_evidence_count=1,
            raw_score=0.2,
            confidence=20.0
        )
    ]

    decision = make_decision(scores)

    assert decision.outcome == "SELECT"
    assert decision.selected_hypotheses == ["H1"]


def test_weak_evidence_abstains():
    scores = [
        HypothesisScore(
            hypothesis_id="H1",
            supporting_weight=0.2,
            contradicting_weight=0.0,
            independent_evidence_count=1,
            raw_score=0.2,
            confidence=20.0
        ),
        HypothesisScore(
            hypothesis_id="H2",
            supporting_weight=0.1,
            contradicting_weight=0.0,
            independent_evidence_count=1,
            raw_score=0.1,
            confidence=10.0
        )
    ]

    decision = make_decision(scores)

    assert decision.outcome == "ABSTAIN"


def test_synthesis_combines_compatible_hypotheses():
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

    score1 = HypothesisScore(
        hypothesis_id="H1",
        supporting_weight=0.9,
        contradicting_weight=0.0,
        independent_evidence_count=1,
        raw_score=0.9,
        confidence=90.0
    )

    score2 = HypothesisScore(
        hypothesis_id="H2",
        supporting_weight=0.8,
        contradicting_weight=0.0,
        independent_evidence_count=1,
        raw_score=0.8,
        confidence=80.0
    )

    result = combine_hypotheses(h1, h2, score1, score2)

    assert result is not None
    assert result.id == "COMBINED_H1_H2"
    assert "Database failure" in result.cause
    assert "Recent software deployment" in result.cause


def test_incompatible_hypotheses_are_not_combined():
    h1 = Hypothesis(
        id="H1",
        cause="Database failure",
        assumptions=["Database is failing"],
        predicted_effects=["Database queries fail"],
        required_evidence=["Database health check"]
    )

    h6 = Hypothesis(
        id="H6",
        cause="Database healthy",
        assumptions=["Database is operating normally"],
        predicted_effects=["Database queries succeed"],
        required_evidence=["Database health check"]
    )

    score1 = HypothesisScore(
        hypothesis_id="H1",
        supporting_weight=0.9,
        contradicting_weight=0.0,
        independent_evidence_count=1,
        raw_score=0.9,
        confidence=90.0
    )

    score6 = HypothesisScore(
        hypothesis_id="H6",
        supporting_weight=0.8,
        contradicting_weight=0.0,
        independent_evidence_count=1,
        raw_score=0.8,
        confidence=80.0
    )

    result = combine_hypotheses(h1, h6, score1, score6)

    assert result is None


def test_discriminating_test_is_recommended():
    h1 = Hypothesis(
        id="H1",
        cause="Database failure"
    )

    h2 = Hypothesis(
        id="H2",
        cause="Recent software deployment"
    )

    result = recommend_discriminating_test(h1, h2)

    assert result is not None
    assert result.description
    assert result.purpose
    assert result.expected_if_h1
    assert result.expected_if_h2


def test_budget_exhaustion():
    budget = InvestigationBudget(
        max_hypotheses=6,
        max_rounds=3,
        max_evidence_checks=10
    )

    assert budget.budget_exhausted() is False

    budget.use_round()
    budget.use_round()
    budget.use_round()

    assert budget.rounds_used == 3
    assert budget.budget_exhausted() is True


def test_stopping_rule():
    budget = InvestigationBudget(
        max_hypotheses=6,
        max_rounds=3,
        max_evidence_checks=10
    )

    scores = [
        HypothesisScore(
            hypothesis_id="H1",
            supporting_weight=0.9,
            contradicting_weight=0.0,
            independent_evidence_count=2,
            raw_score=0.9,
            confidence=90.0
        ),
        HypothesisScore(
            hypothesis_id="H2",
            supporting_weight=0.2,
            contradicting_weight=0.0,
            independent_evidence_count=1,
            raw_score=0.2,
            confidence=20.0
        )
    ]

    stop, reason = should_stop(scores, budget)

    assert stop is True
    assert reason