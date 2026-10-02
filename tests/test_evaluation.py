import json

from src.main import diagnose
from src.evidence import Evidence
from tests.test_calibration import calculate_brier_score

def load_test_cases():

    with open("data/test_cases.json", "r") as file:
        return json.load(file)


def run_evaluation():

    cases = load_test_cases()

    total = len(cases)
    correct = 0
    abstained = 0

    results = []
    calibration_predictions = []

    print("\n" + "=" * 60)
    print("SOFTWARE FAILURE DIAGNOSIS EVALUATION")
    print("=" * 60)

    for case in cases:

        evidence_list = []

        for item in case["evidence"]:

            evidence_list.append(
                Evidence(
                    id=item["id"],
                    description=item["description"],
                    source=item["source"],
                    source_id=item["source_id"],
                    reliability=item["reliability"]
                )
            )

        result = diagnose(
            case["problem"],
            evidence_list
        )

        decision = result["decision"]

        predicted = None

        if decision.selected_hypotheses:
            predicted = decision.selected_hypotheses[0]

        expected = case["expected_cause"]

        is_correct = predicted == expected
        # Get confidence of the selected hypothesis
        confidence = 0

        if decision.selected_hypotheses:

            selected_id = decision.selected_hypotheses[0]

            for score in result["scores"]:

                if score.hypothesis_id == selected_id:
                    confidence = score.confidence
                    break

        calibration_predictions.append(
            (confidence, is_correct)
        )
        
        if is_correct:
            correct += 1

        if decision.outcome == "ABSTAIN":
            abstained += 1

        results.append({
            "case_id": case["case_id"],
            "expected": expected,
            "predicted": predicted,
            "outcome": decision.outcome,
            "correct": is_correct
        })

        print("\n----------------------------------------")
        print(f"Case:      {case['case_id']}")
        print(f"Expected:  {expected}")
        print(f"Predicted: {predicted}")
        print(f"Outcome:   {decision.outcome}")
        print(f"Correct:   {is_correct}")

    accuracy = (correct / total) * 100

    abstention_rate = (abstained / total) * 100

    # Selective accuracy
    non_abstained = total - abstained

    if non_abstained > 0:
        selective_accuracy = (
            correct / non_abstained
        ) * 100
    else:
        selective_accuracy = 0

    # Brier score
    brier_score = calculate_brier_score(
        calibration_predictions
    )

    
    print("\n" + "=" * 60)
    print("FINAL EVALUATION")
    print("=" * 60)

    print(f"Total cases:       {total}")
    print(f"Correct cases:     {correct}")
    print(f"Accuracy:          {accuracy:.2f}%")
    print(f"Abstained cases:   {abstained}")
    print(f"Abstention rate:   {abstention_rate:.2f}%")
    print(
        f"Selective accuracy: "
        f"{selective_accuracy:.2f}%"
    )
    print(
        f"Brier score:       "
        f"{brier_score:.4f}"
        )
    return results


if __name__ == "__main__":
    run_evaluation()