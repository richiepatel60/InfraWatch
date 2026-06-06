from apscheduler.schedulers.background import BackgroundScheduler

from collector import get_system_metrics
from database import insert_metrics
from alerts import check_alerts
from service_watchdog import check_services

def collect_and_store_metrics():

    data = get_system_metrics()

    insert_metrics(data)

    alerts = check_alerts(data)
    missing_services = check_services()
    

    print("Metrics stored:", data)

    if alerts:
        print("ALERTS:", alerts)

    if missing_services:
        print(
            "SERVICE ALERTS:",
            missing_services
    )

def start_scheduler():

    scheduler = BackgroundScheduler()

    scheduler.add_job(
        collect_and_store_metrics,
        'interval',
        seconds=5
    )

    scheduler.start()

    print("Background scheduler started...")