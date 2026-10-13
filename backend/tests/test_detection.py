
import pandas as pd

from app.detection.threshold import detect_threshold_anomalies
from app.detection.rolling import detect_rolling_anomalies
from app.detection.isolation_forest import (
    detect_isolation_forest_anomalies,
)


def test_threshold_detects_high_latency():
    data = pd.DataFrame({
        "latency_ms": [30.0, 45.0, 150.0],
    })

    results = detect_threshold_anomalies(data)

    assert results["is_anomaly"].tolist() == [
        False,
        False,
        True,
    ]


def test_threshold_keeps_normal_sample():
    data = pd.DataFrame({
        "latency_ms": [30.0],
        "packet_loss": [0.5],
    })

    results = detect_threshold_anomalies(data)

    assert results["is_anomaly"].tolist() == [False]


def test_rolling_detects_large_deviation():
    data = pd.DataFrame({
        "latency_ms": [20.0, 21.0, 19.0, 20.0, 100.0],
    })

    results = detect_rolling_anomalies(
        data,
        columns=["latency_ms"],
        window=3,
        z_threshold=2.0,
    )

    assert results["is_anomaly"].iloc[-1]


def test_isolation_forest_returns_predictions():
    data = pd.DataFrame({
        "latency_ms": [
            20.0, 21.0, 19.0, 20.0, 22.0,
            21.0, 19.0, 20.0, 21.0, 200.0,
        ],
    })

    results = detect_isolation_forest_anomalies(
        data,
        columns=["latency_ms"],
        contamination=0.1,
        random_state=42,
    )

    assert "is_anomaly" in results.columns
    assert "anomaly_score" in results.columns
    assert results["is_anomaly"].dtype == bool
    assert len(results) == len(data)
