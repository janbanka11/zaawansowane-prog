from flask import Flask
from flask_restful import Resource, Api
import csv


class Movie:
    def __init__(self, id, title, genres):
        self.id = id
        self.title = title
        self.genres = genres


class Movies:
    def __init__(self):
        with open("movies.csv", newline="") as csvfile:
            spamreader = csv.reader(csvfile, delimiter=" ", quotechar="|")
            i = 0
            for row in spamreader:
                i = i + 1
                print(i)
                print(row)
        # self.movies = movies


Movies = Movies()
# app = Flask(__name__)
# api = Api(app)
#
# class HelloWorld(Resource):
#     def get(self):
#         return {'hello': 'world'}
#
# api.add_resource(HelloWorld, '/')
#
# if __name__ == '__main__':
#     app.run(debug=True)
#
