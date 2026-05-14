from flask import Flask, jsonify, render_template

from collector import get_system_metrics
from database import init_db, get_recent_metrics
from scheduler import start_scheduler

app = Flask(__name__)

init_db()
start_scheduler()


@app.route('/')
def dashboard():
    return render_template('dashboard.html')


@app.route('/api/metrics')
def metrics():

    data = get_system_metrics()

    data["alerts"] = []

    return jsonify(data)

@app.route('/api/history')
def history():

    data = get_recent_metrics()

    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)