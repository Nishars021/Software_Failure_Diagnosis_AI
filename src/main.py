from src.divergence import generate_hypotheses_local
from src.evidence import Evidence, assess_evidence
from src.scoring import calculate_hypothesis_score
from src.stopping import should_stop
from src.budget import InvestigationBudget
from src.decision import make_decision
from src.test_recommender import recommend_discriminating_test


def diagnose(problem, evidence_list):
    print("\n" + "=" * 60)
    print("SOFTWARE FAILURE DIAGNOSIS")
    print("=" * 60)

    print(f"\nProblem: {problem}")

    # --------------------------------------------------
    # 1. Generate hypotheses
    # --------------------------------------------------
    hypotheses = generate_hypotheses_local(problem)

    print("\nGenerated Hypotheses:")
    for h in hypotheses:
        print(f"- {h.id}: {h.cause}")

    # --------------------------------------------------
    # 2. Create investigation budget
    # --------------------------------------------------
    budget = InvestigationBudget(
        max_hypotheses=6,
        max_rounds=3,
        max_evidence_checks=30
    )

    budget.add_hypotheses(len(hypotheses))
    budget.use_round()

    # --------------------------------------------------
    # 3. Assess evidence against hypotheses
    # --------------------------------------------------
    all_scores = []

    print("\nEvidence Analysis:")

    for hypothesis in hypotheses:

        if hypothesis.id == "UNKNOWN":
            continue

        assessments = []

        for evidence in evidence_list:

            if not budget.can_check_evidence():
                break

            assessment = assess_evidence(hypothesis, evidence)
            assessments.append(assessment)

            budget.use_evidence_check()

            print(
                f"{hypothesis.id} | "
                f"{evidence.description} | "
                f"{assessment.evidence_type.value}"
            )

        # --------------------------------------------------
        # 4. Calculate score
        # --------------------------------------------------
        score = calculate_hypothesis_score(
            hypothesis.id,
            assessments
        )

        all_scores.append(score)

    # --------------------------------------------------
    # 5. Display scores
    # --------------------------------------------------
    print("\nHypothesis Scores:")

    for score in all_scores:
        print(
            f"{score.hypothesis_id}: "
            f"confidence={score.confidence:.2f}% | "
            f"raw={score.raw_score:.2f}"
        )

    # --------------------------------------------------
    # 6. Stopping rule
    # --------------------------------------------------
    stop, reason = should_stop(
        all_scores,
        budget
    )

    print("\nStopping Analysis:")
    print(f"Stop: {stop}")
    print(f"Reason: {reason}")

    # --------------------------------------------------
    # 7. Decision
    # --------------------------------------------------
    decision = make_decision(all_scores)

    print("\nDecision:")
    print(f"Outcome: {decision.outcome}")
    print(f"Selected: {decision.selected_hypotheses}")
    print(f"Explanation: {decision.explanation}")

    # --------------------------------------------------
    # 8. Recommend diagnostic test if necessary
    # --------------------------------------------------
    if decision.outcome == "TEST" and len(decision.selected_hypotheses) >= 2:

        h1 = next(
            h for h in hypotheses
            if h.id == decision.selected_hypotheses[0]
        )

        h2 = next(
            h for h in hypotheses
            if h.id == decision.selected_hypotheses[1]
        )

        test = recommend_discriminating_test(h1, h2)

        print("\nRecommended Diagnostic Test:")
        print(f"Test: {test.description}")
        print(f"Purpose: {test.purpose}")
        print(f"If {h1.id}: {test.expected_if_h1}")
        print(f"If {h2.id}: {test.expected_if_h2}")

    return {
        "hypotheses": hypotheses,
        "scores": all_scores,
        "decision": decision,
        "stopping": {
            "stop": stop,
            "reason": reason
        }
    }