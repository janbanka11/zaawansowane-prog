import csv
import time
from model import detect_people

def consume_tasks():
    while True:
        tasks = read_tasks()
        if not tasks:
            print("Consumer: Plik 'tasks.csv' jest pusty.")
            time.sleep(5)
            continue

        for task in tasks:
            if task["status"] == "pending":
                print(f"Consumer: Przetwarzanie zadania {task['id']}")
                task["status"] = "in_progress"
                update_tasks(tasks)

                try:
                    task["result"] = detect_people(task["image_path"])
                    task["status"] = "done"
                    print(f"Consumer: Zadanie {task['id']} zakończone. Liczba osób: {task['result']}")
                except Exception as e:
                    task["status"] = "error"
                    task["error"] = str(e)
                update_tasks(tasks)
        time.sleep(0.1)

def read_tasks():
        with open("tasks.csv", mode="r") as file:
            return list(csv.DictReader(file))


def update_tasks(tasks):
    with open("tasks.csv", mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["id", "image_path", "status", "result", "error"])
        writer.writeheader()
        writer.writerows(tasks)

if __name__ == "__main__":
    consume_tasks()
