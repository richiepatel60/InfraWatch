import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

from legacy.service_watchdog import check_services

print("Running Service Watchdog Test...")

missing_services = check_services()

if not missing_services:
    print("PASS: All watched services are running")
else:
    print("WARNING: Missing services detected")
    print(missing_services)