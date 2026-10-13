from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.detection_result import DetectionResult
from app.models.network_sample import NetworkSample
from app.models.abnormal_event import AbnormalEvent


router = APIRouter(prefix="/evaluation", tags=["Evaluation"])


@router.get("/summary")
def get_evaluation_summary(db: Session = Depends(get_db)):
    total_samples = db.query(NetworkSample).count()
    total_results = db.query(DetectionResult).count()
    total_events = db.query(AbnormalEvent).count()

    methods = (
        db.query(DetectionResult.detection_method)
        .distinct()
        .all()
    )

    method_names = [method[0] for method in methods]

    return {
        "total_network_samples": total_samples,
        "total_detection_results": total_results,
        "total_recorded_events": total_events,
        "methods_evaluated": method_names,
        "note": (
            "Precision, recall, F1-score, and false-positive rate "
            "require labeled evaluation data and are not calculated "
            "by this summary endpoint."
        ),
    }


@router.get("/methods")
def get_method_summary(db: Session = Depends(get_db)):
    methods = (
        db.query(DetectionResult.detection_method)
        .distinct()
        .all()
    )

    summary = []

    for (method_name,) in methods:
        results = (
            db.query(DetectionResult)
            .filter(
                DetectionResult.detection_method == method_name
            )
            .all()
        )

        total = len(results)
        anomalies = sum(
            1 for result in results if result.is_anomaly
        )

        summary.append({
            "method": method_name,
            "total_results": total,
            "anomalies_detected": anomalies,
            "normal_samples": total - anomalies,
        })

    return summary