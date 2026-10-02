from src.scoring import HypothesisScore


def calculate_brier_score(predictions):
    """
    predictions:
        list of tuples:
        (confidence, is_correct)

    confidence should be between 0 and 100.
    """

    if not predictions:
        return 0.0

    total = 0.0

    for confidence, is_correct in predictions:

        probability = confidence / 100

        actual = 1 if is_correct else 0

        total += (probability - actual) ** 2

    return total / len(predictions)


def test_calibration():

    predictions = [
        (90, True),
        (80, True),
        (70, True),
        (60, False),
        (50, True),
        (40, False)
    ]

    score = calculate_brier_score(predictions)

    print("\nBrier Score:", round(score, 4))

    assert 0 <= score <= 1


if __name__ == "__main__":
    test_calibration()