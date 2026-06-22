# enterprise/repositories/db_metrics_repository.py

from enterprise.db.database import SessionLocal
from enterprise.models.metric import Metric


def fetch_recent_metrics(limit=20):

    db = SessionLocal()

    try:

        metrics = (
            db.query(Metric)
            .order_by(Metric.id.desc())
            .limit(limit)
            .all()
        )

        metrics.reverse()

        return [
            {
                "timestamp": metric.timestamp,
                "cpu_percent": metric.cpu_percent,
                "memory_percent": metric.memory_percent,
                "disk_percent": metric.disk_percent
            }
            for metric in metrics
        ]

    finally:

        db.close()