import pandas as pd


DEFAULT_THRESHOLDS = {
    "latency_ms": 100.0,
    "packet_loss": 5.0,
    "cpu_usage": 85.0,
    "memory_usage": 85.0,
    "bandwidth_utilization": 90.0,
}


def detect_threshold_anomalies(
    data: pd.DataFrame,
    thresholds: dict[str, float] | None = None,
) -> pd.DataFrame:
    """Detect network samples that exceed predefined thresholds."""
    limits = thresholds or DEFAULT_THRESHOLDS

    results = data.copy()
    results["is_anomaly"] = False
    results["anomaly_reasons"] = ""

    for metric, limit in limits.items():
        if metric not in results.columns:
            continue

        mask = results[metric] > limit
        results.loc[mask, "is_anomaly"] = True

        reasons = results.loc[mask, "anomaly_reasons"]
        results.loc[mask, "anomaly_reasons"] = reasons.apply(
            lambda value, name=metric: (
                f"{value}, {name} above threshold"
                if value
                else f"{name} above threshold"
            )
        )

    return results