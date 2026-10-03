from src.hypothesis import Hypothesis
from src.scoring import HypothesisScore
from src.stopping import should_stop
from src.budget import InvestigationBudget


h1 = Hypothesis(
    id="H1",
    cause="Database failure"
)

h2 = Hypothesis(
    id="H2",
    cause="Recent software deployment"
)


budget = InvestigationBudget(
    max_hypotheses=6,
    max_rounds=3,
    max_evidence_checks=10
)


print("STOPPING RULE TEST")
print("=" * 60)


# --------------------------------------------------
# TEST 1: Strong leading hypothesis
# --------------------------------------------------

strong_scores = [
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

result1 = should_stop(strong_scores, budget)

print("\nTEST 1: Strong evidence")
print("Stop:", result1)


# --------------------------------------------------
# TEST 2: Weak evidence
# --------------------------------------------------

weak_scores = [
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

result2 = should_stop(weak_scores, budget)

print("\nTEST 2: Weak evidence")
print("Stop:", result2)


# --------------------------------------------------
# TEST 3: Close competing hypotheses
# --------------------------------------------------

close_scores = [
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

result3 = should_stop(close_scores, budget)

print("\nTEST 3: Close competing hypotheses")
print("Stop:", result3)


print("\nSTOPPING RULE TEST COMPLETED")