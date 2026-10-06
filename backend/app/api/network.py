from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.network_sample import NetworkSample
from app.schemas.network_sample import NetworkSampleCreate, NetworkSampleResponse

router = APIRouter(prefix="/network-samples", tags=["Network Samples"])


@router.post("/", response_model=NetworkSampleResponse)
def create_network_sample(
    sample: NetworkSampleCreate,
    db: Session = Depends(get_db),
):
    new_sample = NetworkSample(**sample.model_dump())

    db.add(new_sample)
    db.commit()
    db.refresh(new_sample)

    return new_sample


@router.get("/", response_model=list[NetworkSampleResponse])
def get_network_samples(db: Session = Depends(get_db)):
    return (
        db.query(NetworkSample)
        .order_by(NetworkSample.timestamp.desc())
        .all()
    )