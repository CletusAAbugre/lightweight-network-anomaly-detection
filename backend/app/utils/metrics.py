
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
)


def calculate_classification_metrics(
    actual_labels: list[bool],
    predicted_labels: list[bool],
) -> dict:
    """Calculate classification metrics from labeled evaluation data."""

    if len(actual_labels) != len(predicted_labels):
        raise ValueError(
            "Actual and predicted labels must have the same length."
        )

    if not actual_labels:
        raise ValueError("Evaluation labels cannot be empty.")

    accuracy = accuracy_score(actual_labels, predicted_labels)
    precision = precision_score(
        actual_labels,
        predicted_labels,
        zero_division=0,
    )
    recall = recall_score(
        actual_labels,
        predicted_labels,
        zero_division=0,
    )
    f1 = f1_score(
        actual_labels,
        predicted_labels,
        zero_division=0,
    )

    tn, fp, fn, tp = confusion_matrix(
        actual_labels,
        predicted_labels,
        labels=[False, True],
    ).ravel()

    false_positive_rate = (
        fp / (fp + tn) if (fp + tn) > 0 else 0.0
    )

    return {
        "accuracy": float(accuracy),
        "precision": float(precision),
        "recall": float(recall),
        "f1_score": float(f1),
        "false_positive_rate": float(false_positive_rate),
        "true_positives": int(tp),
        "true_negatives": int(tn),
        "false_positives": int(fp),
        "false_negatives": int(fn),
    }
