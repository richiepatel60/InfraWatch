import sqlite3
from datetime import datetime
from pathlib import Path
from unittest import result

DB_PATH = "data/metrics.db"


def generate_report():

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
    SELECT
    AVG(cpu_percent),
    AVG(memory_percent),
    AVG(disk_percent),

    MAX(cpu_percent),
    MAX(memory_percent),
    MAX(disk_percent),

    COUNT(*),

    MIN(timestamp),
    MAX(timestamp)

    FROM metrics

    WHERE timestamp >= datetime('now', '-7 days')
""")

    result = cursor.fetchone()

    conn.close()

    avg_cpu = round(result[0] or 0, 2)
    avg_memory = round(result[1] or 0, 2)
    avg_disk = round(result[2] or 0, 2)

    peak_cpu = round(result[3] or 0, 2)
    peak_memory = round(result[4] or 0, 2)
    peak_disk = round(result[5] or 0, 2)

    total_records = result[6] or 0
    first_record = result[7] or "N/A"
    last_record = result[8] or "N/A"

    today = datetime.now().strftime("%Y-%m-%d")

    report_file = (
        f"reports/health_report_{today}.txt"
    )

    cpu_alerts = 0
    memory_alerts = 0
    disk_alerts = 0

    try:

        with open(
            "logs/alerts.log",
            "r"
        ) as file:

            lines = file.readlines()

            for line in lines:

                if "CPU" in line:
                    cpu_alerts += 1

                elif "MEMORY" in line:
                    memory_alerts += 1

                elif "DISK" in line:
                    disk_alerts += 1

    except FileNotFoundError:

        pass

    total_alerts = (
        cpu_alerts +
        memory_alerts +
        disk_alerts
    )


    health_score = 100

    if avg_cpu > 80:
        health_score -= 20

    if avg_memory > 85:
        health_score -= 20

    if avg_disk > 90:
        health_score -= 20

    service_down_events = 0

    for key, count in service_events.items():

        service_name, status = key

        if status == "DOWN":
            service_down_events += count

    if service_down_events > 0:
        health_score -= 10

    if health_score < 0:
        health_score = 0
    
    if health_score >= 90:
        overall_status = "HEALTHY"

    elif health_score >= 70:
        overall_status = "GOOD"

    elif health_score >= 50:
        overall_status = "WARNING"

    else:
        overall_status = "CRITICAL"
    
    recommendations = []
    recommendations.append("Report based on last 7 days of monitoring data.")
    if total_alerts == 0:

        recommendations.append(
            "No infrastructure alerts detected."
        )

    if service_down_events == 0:

        recommendations.append(
            "No service outages observed."
        )

    if peak_cpu < 80:

        recommendations.append(
            "CPU utilization remained stable."
        )

    if peak_memory < 85:

        recommendations.append(
            "Memory usage remained within limits."
        )

    recommendation_text = ""

    for item in recommendations:

        recommendation_text += (
            f"• {item}\n"
        )



    report_content = f"""
Infrastructure Health Report

Generated: {datetime.now()}
Report Window: Last 7 Days
--------------------------------

Average CPU Usage: {avg_cpu}%
Average Memory Usage: {avg_memory}%
Average Disk Usage: {avg_disk}%

--------------------------------

Peak CPU Usage: {peak_cpu}%
Peak Memory Usage: {peak_memory}%
Peak Disk Usage: {peak_disk}%

--------------------------------
--------------------------------

Monitoring Statistics

Total Metrics Collected: {total_records}

Monitoring Start:
{first_record}

Monitoring End:
{last_record}

--------------------------------

Overall Status: {overall_status}

--------------------------------

Alert Summary

Total Alerts: {total_alerts}

CPU Alerts: {cpu_alerts}

Memory Alerts: {memory_alerts}

Disk Alerts: {disk_alerts}
--------------------------------

Service Health Summary

{service_summary}
--------------------------------

Health Score

Score: {health_score}/100

Status: {overall_status}
--------------------------------

Recommendations

{recommendation_text}
"""

    with open(report_file, "w") as file:
        file.write(report_content)

    print(
        f"Report generated: {report_file}"
    )



service_events = {}

try:

    with open(
        "logs/service_watchdog.log",
        "r"
    ) as file:

        lines = file.readlines()

        for line in lines:

            if "STATUS CHANGED TO" in line:

                parts = line.split("]")[1].strip()

                service_name = parts.split(
                    "STATUS CHANGED TO"
                )[0].strip()

                status = parts.split(
                    "STATUS CHANGED TO"
                )[1].strip()

                key = (
                    service_name,
                    status
                )

                service_events[key] = (
                    service_events.get(key, 0) + 1
                )

except FileNotFoundError:

    pass

service_summary = ""

for key, count in service_events.items():

    service_name, status = key

    service_summary += (
        f"{service_name} "
        f"{status}: "
        f"{count}\n"
    )

if not service_summary:

    service_summary = (
        "No service events recorded.\n"
    )



if __name__ == "__main__":
    generate_report()