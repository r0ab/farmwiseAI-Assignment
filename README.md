# FarmwiseAI Assignment

This repository contains the code for the FarmwiseAI Assignment. The project is focused on developing a RESTful API for managing a bookstore using Python and the Flask framework.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Authentication](#authentication)


## Introduction

The FarmwiseAI Assignment is a RESTful API designed to manage a bookstore. It allows users to perform CRUD operations on book information, such as adding new books, retrieving all books, updating book details, and deleting books. The project is implemented in Python using the Flask framework.

## Features

- Add new books to the store
- Retrieve information about all books
- Retrieve information about a specific book by ISBN
- Update details of existing books
- Delete books from the store
- Basic authentication for certain endpoints
- JWT token-based authentication (bonus)

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python (version >= 3.x)
- Flask framework


### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/r0ab/farmwiseAI-Assignment.git
   cd farmwiseAI-Assignment
Install dependencies:

bash

pip install -r requirements.txt
Run the Flask application:

bash

python app.py
The API should now be accessible at http://127.0.0.1:5000/.

### Usage


### API Endpoints
GET /books: Retrieve information about all books.
POST /books: Add a new book to the store.
GET /books/int:book_id: Retrieve information about a specific book by ID.
PUT /books/int:book_id: Update details of an existing book.
DELETE /books/int:book_id: Delete a book from the store.
(Include any additional endpoints and descriptions as needed.)

### Authentication
The FarmwiseAI Assignment project incorporates authentication to secure certain endpoints. There are two main authentication mechanisms implemented:

1. Basic Authentication
Some endpoints require basic authentication to restrict access. Users are required to provide a valid username and password to access these protected endpoints.

Example:

bash
Copy code
curl -X GET http://127.0.0.1:5000/books -u username:password

2. JWT Token-Based Authentication (Bonus Points Achieved)
In addition to basic authentication, the project supports JSON Web Token (JWT) token-based authentication. This adds an extra layer of security, especially for sensitive operations.

Workflow:

Login Endpoint: Users can obtain a JWT token by sending a POST request to the login endpoint with valid credentials.

bash

curl -X POST http://127.0.0.1:5000/login -u username:password
Successful login will return a JSON response containing the JWT token.

Use Token in Requests: To access protected endpoints, include the obtained JWT token in the Authorization header with the "Bearer" type.

bash
Copy code
curl -X GET http://127.0.0.1:5000/books -H "Authorization: Bearer <JWT_TOKEN>"
Example:

bash

curl -X GET http://127.0.0.1:5000/books -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...."
This token is used for subsequent requests to prove the identity of the user.

Note: Token-based authentication provides a stateless way to authenticate users, reducing the need to store session data on the server.
