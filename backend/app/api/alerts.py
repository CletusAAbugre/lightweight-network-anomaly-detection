from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.alert import Alert
from app.models.detection_result import DetectionResult
from app.schemas.alert import AlertCreate, AlertResponse


router = APIRouter(prefix="/alerts", tags=["Alerts"])


@router.post("/", response_model=AlertResponse)
def create_alert(
    alert: AlertCreate,
    db: Session = Depends(get_db),
):
    detection = db.query(DetectionResult).filter(
        DetectionResult.id == alert.detection_result_id
    ).first()

    if detection is None:
        raise HTTPException(
            status_code=404,
            detail="Detection result not found.",
        )

    new_alert = Alert(**alert.model_dump())

    db.add(new_alert)
    db.commit()
    db.refresh(new_alert)

    return new_alert


@router.get("/", response_model=list[AlertResponse])
def get_alerts(db: Session = Depends(get_db)):
    return (
        db.query(Alert)
        .order_by(Alert.created_at.desc())
        .all()
    )


@router.patch("/{alert_id}/acknowledge", response_model=AlertResponse)
def acknowledge_alert(
    alert_id: int,
    db: Session = Depends(get_db),
):
    alert = db.query(Alert).filter(Alert.id == alert_id).first()

    if alert is None:
        raise HTTPException(
            status_code=404,
            detail="Alert not found.",
        )

    alert.is_acknowledged = True

    db.commit()
    db.refresh(alert)

    return alert