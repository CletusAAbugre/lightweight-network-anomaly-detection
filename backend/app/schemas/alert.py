from datetime import datetime

from pydantic import BaseModel, ConfigDict


class AlertBase(BaseModel):
    detection_result_id: int
    message: str
    severity: str = "medium"
    is_acknowledged: bool = False


class AlertCreate(AlertBase):
    pass


class AlertResponse(AlertBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)