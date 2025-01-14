import csv
import os
import time

def consumer():
    file_name = "tasks.csv"
    if not os.path.exists(file_name):
        print("File doesn't exist.")
        return

    while True:
        tasks = []
        work_done = False

        with open(file_name, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            tasks = list(reader)
        for task in tasks:
            if task["status"] == "pending":
                print(f"Consumer: Task start: {task['task']}")

                task["status"] = "in_progress"
                work_done = True
                _update_file(file_name, tasks)
                time.sleep(30)
                task["status"] = "done"
                print(f"Consumer: Task done: {task['task']}")
                _update_file(file_name, tasks)
                break

        if not work_done:
            print("Consumer: No tasks")
        time.sleep(5)

def _update_file(file_name, tasks):
    with open(file_name, mode="w", newline="") as file:
        fieldnames = ["id", "task", "status", "created_at"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(tasks)

if __name__ == "__main__":
    consumer()
