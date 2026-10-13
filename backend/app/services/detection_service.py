import pandas as pd
from sqlalchemy.orm import Session

from app.models.network_sample import NetworkSample
from app.models.detection_result import DetectionResult
from app.detection import (
    detect_threshold_anomalies,
    detect_rolling_anomalies,
    detect_isolation_forest_anomalies,
)


DETECTION_METHODS = {
    "threshold": detect_threshold_anomalies,
    "rolling": detect_rolling_anomalies,
    "isolation_forest": detect_isolation_forest_anomalies,
}


def run_detection(
    db: Session,
    method: str = "threshold",
) -> list[DetectionResult]:
    """Run a detection method on stored samples and save its results."""

    detector = DETECTION_METHODS.get(method)

    if detector is None:
        raise ValueError(
            "Unsupported method. Use threshold, rolling, or isolation_forest."
        )

    samples = (
        db.query(NetworkSample)
        .order_by(NetworkSample.timestamp.asc())
        .all()
    )

    if not samples:
        return []

    data = pd.DataFrame([
        {
            "id": sample.id,
            "active_users": sample.active_users,
            "download_mbps": sample.download_mbps,
            "upload_mbps": sample.upload_mbps,
            "bandwidth_utilization": sample.bandwidth_utilization,
            "latency_ms": sample.latency_ms,
            "packet_loss": sample.packet_loss,
            "cpu_usage": sample.cpu_usage,
            "memory_usage": sample.memory_usage,
        }
        for sample in samples
    ])

    results = detector(data)
    saved_results = []

    try:
        for _, row in results.iterrows():
            score = row.get("anomaly_score")
            reason = row.get("anomaly_reasons", "")

            detection = DetectionResult(
                network_sample_id=int(row["id"]),
                detection_method=method,
                is_anomaly=bool(row["is_anomaly"]),
                anomaly_score=(
                    float(score) if pd.notna(score) else None
                ),
                anomaly_reason=str(reason) if reason else None,
            )

            db.add(detection)
            saved_results.append(detection)

        db.commit()

        for detection in saved_results:
            db.refresh(detection)

        return saved_results

    except Exception:
        db.rollback()
        raise