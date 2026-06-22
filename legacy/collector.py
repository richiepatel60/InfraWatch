import psutil
from datetime import datetime


def get_system_metrics():

    metrics = {

        "timestamp": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ),

        "cpu_percent": psutil.cpu_percent(),

        "memory_percent": psutil.virtual_memory().percent,

        "disk_percent": psutil.disk_usage('/').percent,

        "process_count": len(psutil.pids())
    }

    return metrics


if __name__ == "__main__":

    data = get_system_metrics()

    print(data)