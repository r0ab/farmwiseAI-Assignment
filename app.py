from flask import Flask, jsonify, request
from http import HTTPStatus
from book_store import books
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this in a production environment
jwt = JWTManager(app)

# Database (for now, using an in-memory list as a placeholder)
# In a real-world scenario, you would use a database like SQLite or PostgreSQL
books_db = []


# Basic Authentication Middleware
@app.before_request
def authenticate():
    # Exclude authentication for specific routes
    if request.endpoint and request.endpoint in ['login']:
        return
    
    auth = request.authorization
    if not auth or not (auth.username == 'admin' and auth.password == 'password'):
        return jsonify({'message': 'Authentication failed'}), HTTPStatus.UNAUTHORIZED



# CRUD Endpoints
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify({'data': books_db})


@app.route('/books', methods=['POST'])
@jwt_required()
def create_book():
    data = request.get_json()

    title = data.get('book_title')
    author = data.get('book_author')
    publisher = data.get('publisher')
    description = data.get('description')

    book = {
        "id": len(books_db) + 1,
        "title": title,
        "author": author,
        'publisher': publisher,
        'description': description
    }

    books_db.append(book)

    return jsonify({'data': books_db}), HTTPStatus.CREATED


@app.route('/books/<int:book_id>', methods=['PUT'])
@jwt_required()
def update_book(book_id):
    book = next((book for book in books_db if book['id'] == book_id), None)

    if not book:
        return jsonify({'message': "Book not found"}), HTTPStatus.NOT_FOUND

    data = request.get_json()
    book.update(
        {
            'title': data.get('book_title'),
            'author': data.get('book_author'),
            'publisher': data.get('publisher'),
            'description': data.get('description'),
        }
    )

    return jsonify({'data': book})


@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books_db if book['id'] == book_id), None)

    if book:
        return jsonify({'data': book})
    return jsonify({"message": "Book not found"}), HTTPStatus.NOT_FOUND


@app.route('/books/isbn/<isbn>', methods=['GET'])
def get_book_by_isbn(isbn):
    book = next((book for book in books_db if book.get('isbn') == isbn), None)

    if book:
        return jsonify({'data': book})
    return jsonify({"message": "Book not found"}), HTTPStatus.NOT_FOUND


# JWT Token Generation (Login) Endpoint
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # In a real-world scenario, you'd validate the username and password against a user database
    if username == 'admin' and password == 'password':
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), HTTPStatus.OK
    else:
        return jsonify({'message': 'Invalid credentials'}), HTTPStatus.UNAUTHORIZED


# JWT Token Validation
@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload):
    jti = jwt_payload['jti']
    return jti in revoked_tokens


if __name__ == '__main__':
    app.run(debug=True)


# {
#   "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcwNjE4NDUxNywianRpIjoiMzVhNDE4YzgtODNmOC00YmQzLTllMjgtMmM1NjMzZDQwNmFkIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImFkbWluIiwibmJmIjoxNzA2MTg0NTE3LCJjc3JmIjoiMWU2ZjE1NDMtYTY5NS00Y2ExLTg1NDQtN2NhZTU2ZmEwZTljIiwiZXhwIjoxNzA2MTg1NDE3fQ.op_31OZLYl6Pudb_cOWfhYPbXP-dZYQfcmJbinfnKR0"
# }
