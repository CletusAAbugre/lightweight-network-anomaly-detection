from datetime import datetime

from pydantic import BaseModel, ConfigDict


class DetectionResultBase(BaseModel):
    network_sample_id: int
    detection_method: str
    is_anomaly: bool
    anomaly_score: float | None = None
    anomaly_reason: str | None = None


class DetectionResultCreate(DetectionResultBase):
    pass


class DetectionResultResponse(DetectionResultBase):
    id: int
    detected_at: datetime

    model_config = ConfigDict(from_attributes=True)