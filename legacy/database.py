import sqlite3
from pathlib import Path


DB_PATH = Path("data/metrics.db")


def init_db():

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS metrics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            cpu_percent REAL,
            memory_percent REAL,
            disk_percent REAL,
            process_count INTEGER
        )
    """)

    conn.commit()
    conn.close()


def insert_metrics(data):

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO metrics (
            timestamp,
            cpu_percent,
            memory_percent,
            disk_percent,
            process_count
        )
        VALUES (?, ?, ?, ?, ?)
    """, (
        data['timestamp'],
        data['cpu_percent'],
        data['memory_percent'],
        data['disk_percent'],
        data['process_count']
    ))

    conn.commit()
    conn.close()

def get_recent_metrics(limit=20):

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            timestamp,
            cpu_percent,
            memory_percent,
            disk_percent
        FROM metrics
        ORDER BY id DESC
        LIMIT ?
    """, (limit,))

    rows = cursor.fetchall()

    conn.close()

    rows.reverse()

    history = []

    for row in rows:

        history.append({
            "timestamp": row[0],
            "cpu_percent": row[1],
            "memory_percent": row[2],
            "disk_percent": row[3]
        })

    return history