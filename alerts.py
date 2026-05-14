from datetime import datetime


ALERT_LOG_FILE = "logs/alerts.log"


def check_alerts(metrics):

    alerts = []

    if metrics["cpu_percent"] > 80:
        alerts.append(
            f"HIGH CPU USAGE: {metrics['cpu_percent']}%"
        )

    if metrics["memory_percent"] > 85:
        alerts.append(
            f"HIGH MEMORY USAGE: {metrics['memory_percent']}%"
        )

    if metrics["disk_percent"] > 90:
        alerts.append(
            f"HIGH DISK USAGE: {metrics['disk_percent']}%"
        )

    if alerts:
        write_alerts(alerts)

    return alerts


def write_alerts(alerts):

    with open(ALERT_LOG_FILE, "a") as file:

        for alert in alerts:

            timestamp = datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

            log_entry = f"[{timestamp}] {alert}\n"

            file.write(log_entry)