
import pytest

from app.utils.metrics import calculate_classification_metrics


def test_classification_metrics():
    result = calculate_classification_metrics(
        [False, False, True, True],
        [False, True, True, True],
    )

    assert result["accuracy"] == 0.75
    assert result["precision"] == pytest.approx(2 / 3)
    assert result["recall"] == 1.0
    assert result["f1_score"] == 0.8
    assert result["false_positive_rate"] == 0.5


def test_perfect_predictions():
    result = calculate_classification_metrics(
        [False, False, True, True],
        [False, False, True, True],
    )

    assert result["accuracy"] == 1.0
    assert result["precision"] == 1.0
    assert result["recall"] == 1.0
    assert result["f1_score"] == 1.0
    assert result["false_positive_rate"] == 0.0


def test_mismatched_label_lengths():
    with pytest.raises(ValueError, match="same length"):
        calculate_classification_metrics(
            [False, True],
            [False],
        )


def test_empty_labels():
    with pytest.raises(ValueError, match="cannot be empty"):
        calculate_classification_metrics([], [])
