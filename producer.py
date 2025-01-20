import os
import csv

def produce_tasks():
    image_paths = [os.path.join("pictures", file) for file in os.listdir("pictures") if file.endswith((".jpg", ".png"))][:1000]
    if len(image_paths) < 1000:
        raise ValueError("pictures size < 1000")

    with open("tasks.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["id", "image_path", "status"])
        for i, image_path in enumerate(image_paths, start=1):
            writer.writerow([i, image_path, "pending"])
            print(f"Zadanie {i} dodane: {image_path}")

if __name__ == "__main__":
    produce_tasks()
