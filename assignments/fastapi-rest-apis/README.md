# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a simple REST API using FastAPI and Python. In this assignment, you will learn how to create endpoints, validate request data, and return structured JSON responses.

## 📝 Tasks

### 🛠️	Create Core API Endpoints

#### Description
Set up a FastAPI app and implement the core endpoints for managing a small collection of books. Start with in-memory data so you can focus on API design and request/response flow.

#### Requirements
Completed program should:

- Create a FastAPI app instance.
- Implement `GET /` that returns a welcome message.
- Implement `GET /books` that returns all books.
- Implement `GET /books/{book_id}` that returns one book by id.
- Return a clear 404 response when a book id is not found.


### 🛠️	Add Create and Update Operations

#### Description
Add endpoints that allow clients to create and update books. Use Pydantic models to validate incoming JSON and return consistent responses.

#### Requirements
Completed program should:

- Define a Pydantic model for book input data.
- Implement `POST /books` to add a new book.
- Implement `PUT /books/{book_id}` to update an existing book.
- Validate required fields and data types using FastAPI/Pydantic.
- Return JSON responses that include the created or updated book data.
