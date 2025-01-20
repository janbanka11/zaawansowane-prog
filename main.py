import csv

from flask import Flask, abort
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class TaskStatus(Resource):
    def get(self, task_id):
        try:
            with open("tasks.csv", mode="r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if int(row["id"]) == task_id:
                        return {
                            "task_id": task_id,
                            "status": row["status"],
                            "result": row.get("result"),
                            "error": row.get("error")
                        }, 200
        except FileNotFoundError:
            abort(404, description="Nie znaleziono pliku tasks.csv")

api.add_resource(TaskStatus, '/status/<int:task_id>')

if __name__ == '__main__':
    app.run(debug=True)
