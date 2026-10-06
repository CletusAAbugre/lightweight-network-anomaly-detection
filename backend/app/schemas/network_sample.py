from datetime import datetime

from pydantic import BaseModel, ConfigDict


class NetworkSampleBase(BaseModel):
    timestamp: datetime
    active_users: int
    download_mbps: float
    upload_mbps: float
    bandwidth_utilization: float
    latency_ms: float
    packet_loss: float
    cpu_usage: float
    memory_usage: float
    device_status: str


class NetworkSampleCreate(NetworkSampleBase):
    pass


class NetworkSampleResponse(NetworkSampleBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
