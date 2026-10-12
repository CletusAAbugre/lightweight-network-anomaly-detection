from datetime import datetime

from sqlalchemy import DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class DetectionResult(Base):
    __tablename__ = "detection_results"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    network_sample_id: Mapped[int] = mapped_column(
        ForeignKey("network_samples.id"),
        nullable=False,
    )

    detection_method: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    is_anomaly: Mapped[bool] = mapped_column(
        nullable=False,
    )

    anomaly_score: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    anomaly_reason: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    detected_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )