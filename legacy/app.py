from flask import Flask, jsonify, render_template, send_file
from datetime import datetime

from legacy.collector import get_system_metrics
from legacy.database import init_db, get_recent_metrics
from scheduler import start_scheduler
from legacy.service_watchdog import get_service_status
from legacy.report_generator import generate_report

app = Flask(__name__)

import os

init_db()

if os.environ.get("WERKZEUG_RUN_MAIN") == "true":
    start_scheduler()


@app.route('/')
def dashboard():
    return render_template('dashboard.html')


@app.route('/api/metrics')
def metrics():

    data = get_system_metrics()

    data["alerts"] = []

    health_score = 100

    if data["cpu_percent"] > 80:
        health_score -= 20

    if data["memory_percent"] > 85:
        health_score -= 20

    if data["disk_percent"] > 90:
        health_score -= 20

    if health_score >= 90:
        status = "EXCELLENT"

    elif health_score >= 75:
        status = "GOOD"

    elif health_score >= 50:
        status = "WARNING"

    else:
        status = "CRITICAL"

    data["health_score"] = health_score

    data["health_status"] = status

    return jsonify(data)

@app.route('/api/history')
def history():

    data = get_recent_metrics()

    return jsonify(data)

@app.route('/api/services')
def services():

    return jsonify(
        get_service_status()
    )

@app.route('/api/generate-report')
def generate_report_api():

    generate_report()

    return jsonify({

        "message":
        "Report Generated Successfully"

    })

@app.route('/api/download-report')
def download_report():

    today = datetime.now().strftime("%Y-%m-%d")

    report_path = (
        f"reports/health_report_{today}.txt"
    )

    return send_file(
        report_path,
        as_attachment=True
    )

if __name__ == '__main__':
    app.run(debug=True)