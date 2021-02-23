from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

books = {
  '1': {'title': 'War and Peace'},
  '2': {'title': 'Moby Dick'},
  '3': {'title': 'Brave New World'},
  '4': {'title': 'Crime and Punishment'},
  '5': {'title': 'The Call of the Wild'},
}

@app.route('/welcome')
def welcome():
    return "Welcome"

@app.route('/book')
def book():
    return books

class Books(Resource):
    def get(self, book_id):
        if book_id not in books:
            return 'Not found'
        else:
            return books[book_id]

api.add_resource(Books, '/book/<book_id>')

if __name__ == "__main__":
  app.run(debug=True)