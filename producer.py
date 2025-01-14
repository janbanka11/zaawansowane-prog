import csv
import os
import time
import uuid
from datetime import datetime

def producer():
    file_name = "tasks.csv"

    if not os.path.exists(file_name):
        with open(file_name, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["id", "task", "status", "created_at"])

    while True:
        task_description = f"Task {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        task_status = "pending"
        task_created_at = datetime.now().isoformat()
        with open(file_name, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([task_description, task_status, task_created_at])

        print(f"Producer: New task add: {task_description}")
        time.sleep(5)

if __name__ == "__main__":
    producer()
