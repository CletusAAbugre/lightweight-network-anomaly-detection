import pandas as pd


def detect_rolling_anomalies(
    data: pd.DataFrame,
    columns: list[str] | None = None,
    window: int = 5,
    z_threshold: float = 3.0,
) -> pd.DataFrame:
    """Detect values that deviate strongly from previous observations."""
    results = data.copy()

    if columns is None:
        columns = [
            "active_users",
            "download_mbps",
            "upload_mbps",
            "bandwidth_utilization",
            "latency_ms",
            "packet_loss",
            "cpu_usage",
            "memory_usage",
        ]

    results["is_anomaly"] = False
    results["anomaly_reasons"] = ""

    for column in columns:
        if column not in results.columns:
            continue

        previous_values = results[column].shift(1)

        rolling_mean = previous_values.rolling(
            window=window,
            min_periods=window,
        ).mean()

        rolling_std = previous_values.rolling(
            window=window,
            min_periods=window,
        ).std()

        z_score = (
            (results[column] - rolling_mean)
            / rolling_std.replace(0, pd.NA)
        )

        mask = (z_score.abs() > z_threshold).fillna(False)

        results.loc[mask, "is_anomaly"] = True

        results.loc[mask, "anomaly_reasons"] = (
            results.loc[mask, "anomaly_reasons"]
            .apply(
                lambda value, name=column: (
                    f"{value}, {name} deviates from rolling baseline"
                    if value
                    else f"{name} deviates from rolling baseline"
                )
            )
        )

    return results