from fastapi import APIRouter

from enterprise.services.metrics_service import (
    get_live_metrics,
    get_metrics_history
)

router = APIRouter()


@router.get("/metrics")
def read_metrics():

    return get_live_metrics()


@router.get("/history")
def history():

    return get_metrics_history()