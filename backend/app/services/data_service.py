from sqlalchemy.orm import Session

from app.models.network_sample import NetworkSample


def get_network_samples(
    db: Session,
    limit: int = 1000,
) -> list[NetworkSample]:
    """Return recent network samples, newest first."""
    return (
        db.query(NetworkSample)
        .order_by(NetworkSample.timestamp.desc())
        .limit(limit)
        .all()
    )


def get_network_sample_by_id(
    db: Session,
    sample_id: int,
) -> NetworkSample | None:
    """Return a network sample by its ID."""
    return (
        db.query(NetworkSample)
        .filter(NetworkSample.id == sample_id)
        .first()
    )


def count_network_samples(db: Session) -> int:
    """Return the total number of stored network samples."""
    return db.query(NetworkSample).count()