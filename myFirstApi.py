from flask import Flask, jsonify, request, make_response
import dataset

# Create an instance of the class
app = Flask(__name__)

# This will create a database file called 'books.db'
db = dataset.connect('sqlite:///api.db')

# Creating a table in our 'api' database called 'books'
table = db['books']

def fetch_db(book_id): # Each book scenario
    return table.find_one(book_id=book_id)

def fetch_db_all():
    books = []
    for book in table:
        books.append(book)
    return books

# We need to setup and endpoint for the database so that it only sets up the database one and not when it gets reloaded or else the contents will be rem
@app.route('/api/books/db_populate')
def db_populate():

    # We will now insert two bits of information from our dictionary before
    table.insert({
            "book_id": "1",
            "name": "A Game of Thrones",
            "author": "George R. R. Martin"
        })

    table.insert({
            "book_id": "2",
            "name": "Lord of the Rings",
            "author": "J. R. R. Tolkien"
        })
    return make_response(jsonify(fetch_db_all()),200) 

# REPLACE: All 'books variables replaced with: fetch_db_all()
# REPLACE: All 'book_obj' with: fetch_db()

@app.route('/api/books', methods=['GET', 'POST'])
def api_books():
    if request.method == "GET":
        return make_response(jsonify(fetch_db_all()),200)
    elif request.method == "POST":
        content = request.json
        book_id = content['book_id']
        table.insert(content)
        return make_response(jsonify(fetch_db(book_id)), 201) #201 = Creates book

@app.route('/api/books/<book_id>', methods=['GET', 'PUT', 'DELETE'])
def api_each_book(book_id):
    if request.method == "GET":
        book_obj = fetch_db(book_id)
        if book_obj: # if the book is present
            return make_response(jsonify(book_obj),200) # it is there
        else:
            return make_response(jsonify(book_obj),404) # doesn't exist

    elif request.method == "PUT": # Updates the book
        content = request.json
        table.update(content, ['book_id'])

        # books[book_id] = fetch_db(book_id)
        book_obj = fetch_db(book_id)
        return make_response(jsonify(book_obj), 200)

    elif request.method == "DELETE":
        table.delete(id=book_id)
        return make_response(jsonify({}), 204)

if __name__ == '__main__':
    app.run(debug=True)