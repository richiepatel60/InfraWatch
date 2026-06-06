import psutil
from datetime import datetime

SERVICE_STATUS = {}

WATCHED_SERVICES = [
    "Google Chrome",
    "Code"
]

LOG_FILE = "logs/service_watchdog.log"

def check_services():

    running_processes = []

    for proc in psutil.process_iter(['name']):
        try:
            if proc.info['name']:
                running_processes.append(proc.info['name'])
        except:
            pass

    state_changes = []

    for service in WATCHED_SERVICES:

        currently_running = False

        for process in running_processes:

            if service.lower() in process.lower():
                currently_running = True
                break

        previous_status = SERVICE_STATUS.get(
            service,
            "UNKNOWN"
        )

        current_status = (
            "UP"
            if currently_running
            else "DOWN"
        )

        if previous_status != current_status:

            SERVICE_STATUS[service] = current_status

            state_changes.append({
                "service": service,
                "status": current_status
            })

    if state_changes:
        write_service_events(state_changes)

    return state_changes


def write_service_events(events):

    with open(LOG_FILE, "a") as file:

        for event in events:

            timestamp = datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

            file.write(
                f"[{timestamp}] "
                f"{event['service']} "
                f"STATUS CHANGED TO "
                f"{event['status']}\n"
            )

def get_service_status():

    return SERVICE_STATUS