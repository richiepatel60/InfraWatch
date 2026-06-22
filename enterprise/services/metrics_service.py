from legacy.collector import get_system_metrics

from enterprise.repositories.metrics_repository import (
    fetch_recent_metrics
)


def get_live_metrics():

    return get_system_metrics()


def get_metrics_history():

    return fetch_recent_metrics()