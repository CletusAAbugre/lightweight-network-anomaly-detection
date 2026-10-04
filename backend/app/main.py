from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Lightweight Network Anomaly Detection API",
    description="Backend API for detecting network anomalies in small MikroTik-based hotspot networks.",
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
