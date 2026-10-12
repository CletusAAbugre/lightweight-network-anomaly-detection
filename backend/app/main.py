
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.models.network_sample import NetworkSample
from app.models.detection_result import DetectionResult
from app.models.alert import Alert
from app.models.abnormal_event import AbnormalEvent
from app.api.network import router as network_router
from app.api.anomalies import router as anomalies_router
from app.api.alerts import router as alerts_router


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Lightweight Network Anomaly Detection API",
    description=(
        "Backend API for detecting network anomalies "
        "in small MikroTik-based hotspot networks."
    ),
    version="0.1.0",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        "message": "Lightweight Network Anomaly Detection API",
        "status": "running",
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}


app.include_router(network_router)
app.include_router(anomalies_router)
app.include_router(alerts_router)
