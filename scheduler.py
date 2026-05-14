from apscheduler.schedulers.background import BackgroundScheduler

from collector import get_system_metrics
from database import insert_metrics
from alerts import check_alerts


def collect_and_store_metrics():

    data = get_system_metrics()

    insert_metrics(data)

    alerts = check_alerts(data)

    print("Metrics stored:", data)

    if alerts:
        print("ALERTS:", alerts)


def start_scheduler():

    scheduler = BackgroundScheduler()

    scheduler.add_job(
        collect_and_store_metrics,
        'interval',
        seconds=5
    )

    scheduler.start()

    print("Background scheduler started...")