from fastapi import APIRouter

from enterprise.services.metrics_service import (
    get_live_metrics
)

router = APIRouter()


@router.get("/metrics")
def read_metrics():

    return get_live_metrics()