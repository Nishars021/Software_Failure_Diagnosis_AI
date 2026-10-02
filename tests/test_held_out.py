import json

from src.main import diagnose
from src.evidence import Evidence


def load_cases():

    with open("data/held_out_cases.json", "r") as file:
        return json.load(file)


def run_held_out_evaluation():

    cases = load_cases()

    total = len(cases)
    correct = 0

    print("\n" + "=" * 60)
    print("HELD-OUT EVALUATION")
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

        # UNKNOWN is correctly handled by ABSTAIN
        if expected == "UNKNOWN":
            is_correct = (
                predicted is None
                and decision.outcome == "ABSTAIN"
            )
        else:
            is_correct = predicted == expected

        if is_correct:
            correct += 1

        print("\n------------------------------")
        print(f"Case:      {case['case_id']}")
        print(f"Expected:  {expected}")
        print(f"Predicted: {predicted}")
        print(f"Outcome:   {decision.outcome}")
        print(f"Correct:   {is_correct}")

    accuracy = (correct / total) * 100

    print("\n" + "=" * 60)
    print("HELD-OUT RESULTS")
    print("=" * 60)

    print(f"Total cases:   {total}")
    print(f"Correct:       {correct}")
    print(f"Accuracy:      {accuracy:.2f}%")


if __name__ == "__main__":
    run_held_out_evaluation()