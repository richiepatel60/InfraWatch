# InfraWatch – Linux Monitoring Platform

InfraWatch is a lightweight infrastructure monitoring and observability platform built using Python, Flask, SQLite, and psutil.

The platform collects real-time Linux/macOS system telemetry, stores historical metrics, visualizes operational health through dashboards, and generates threshold-based alerts for infrastructure monitoring.

---

## Features

- Real-time CPU, memory, disk, and process monitoring
- Flask-based REST APIs for telemetry access
- Historical metric storage using SQLite
- Background metric collection scheduler
- Threshold-based operational alerting
- Live dashboard with auto-refreshing metrics
- Historical trend visualization using Chart.js
- Alert logging and monitoring workflows

---

## Tech Stack

- Python
- Flask
- SQLite
- APScheduler
- psutil
- Bootstrap
- Chart.js

---

## Project Architecture

System Metrics
↓
psutil Collector
↓
Background Scheduler
↓
SQLite Storage
↓
Flask APIs
↓
Dashboard + Charts + Alerts

---

## API Endpoints

### Live Metrics

```bash
/api/metrics
```

Returns current system telemetry.

### Historical Metrics

```bash
/api/history
```

Returns recent historical metrics for chart visualization.

---

## Setup Instructions

### Clone Repository

```bash
git clone <your-repo-url>
cd InfraWatch
```

### Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python3 app.py
```

Open:

```bash
http://127.0.0.1:5000
```

---

## Future Improvements

- Network monitoring
- Docker containerization
- Multi-node monitoring
- Prometheus integration
- Grafana dashboards
- WebSocket real-time streaming

---

## Dashboard Preview

![InfraWatch Dashboard](screenshots/dashboard.png)
