
import pandas as pd
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.network_sample import NetworkSample
from app.models.detection_result import DetectionResult
from app.schemas.detection_result import DetectionResultResponse
from app.detection.threshold import detect_threshold_anomalies
from app.detection.rolling import detect_rolling_anomalies
from app.detection.isolation_forest import detect_isolation_forest_anomalies


router = APIRouter(prefix="/anomalies", tags=["Anomalies"])


@router.post("/detect", response_model=list[DetectionResultResponse])
def detect_anomalies(
    method: str = "threshold",
    db: Session = Depends(get_db),
):
    samples = (
        db.query(NetworkSample)
        .order_by(NetworkSample.timestamp.asc())
        .all()
    )

    if not samples:
        raise HTTPException(
            status_code=400,
            detail="No network samples available for detection.",
        )

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

    if method == "threshold":
        results = detect_threshold_anomalies(data)
    elif method == "rolling":
        results = detect_rolling_anomalies(data)
    elif method == "isolation_forest":
        results = detect_isolation_forest_anomalies(data)
    else:
        raise HTTPException(
            status_code=400,
            detail="Unsupported method. Use threshold, rolling, or isolation_forest.",
        )

    saved_results = []

    for _, row in results.iterrows():
        reasons = row.get("anomaly_reasons", "")
        score = row.get("anomaly_score")

        detection = DetectionResult(
            network_sample_id=int(row["id"]),
            detection_method=method,
            is_anomaly=bool(row["is_anomaly"]),
            anomaly_score=float(score) if pd.notna(score) else None,
            anomaly_reason=str(reasons) if reasons else None,
        )

        db.add(detection)
        db.flush()
        saved_results.append(detection)

    db.commit()

    for detection in saved_results:
        db.refresh(detection)

    return saved_results
