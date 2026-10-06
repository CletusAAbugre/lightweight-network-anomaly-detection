import pandas as pd
from sklearn.ensemble import IsolationForest


DEFAULT_FEATURES = [
    "active_users",
    "download_mbps",
    "upload_mbps",
    "bandwidth_utilization",
    "latency_ms",
    "packet_loss",
    "cpu_usage",
    "memory_usage",
]


def detect_isolation_forest_anomalies(
    data: pd.DataFrame,
    columns: list[str] | None = None,
    contamination: float = 0.05,
    n_estimators: int = 100,
    random_state: int = 42,
) -> pd.DataFrame:
    """Detect unusual network samples using Isolation Forest."""

    results = data.copy()

    if columns is None:
        columns = DEFAULT_FEATURES

    available_columns = [
        column for column in columns
        if column in results.columns
    ]

    if not available_columns:
        raise ValueError("No valid detection features were found.")

    model = IsolationForest(
        n_estimators=n_estimators,
        contamination=contamination,
        random_state=random_state,
    )

    predictions = model.fit_predict(results[available_columns])

    results["is_anomaly"] = predictions == -1
    results["anomaly_score"] = model.decision_function(
        results[available_columns]
    )

    results["anomaly_reasons"] = results["is_anomaly"].apply(
        lambda value: (
            "Isolation Forest detected unusual network behavior"
            if value
            else ""
        )
    )

    return results