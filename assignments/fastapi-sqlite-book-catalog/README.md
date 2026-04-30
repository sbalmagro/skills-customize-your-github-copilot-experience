# 📘 Assignment: FastAPI SQLite Book Catalog

## 🎯 Objective

Build a beginner-friendly REST API that stores books in a SQLite database using FastAPI and SQLModel. You will learn how to connect an API to persistent data and implement basic CRUD endpoints.

## 📝 Tasks

### 🛠️	Set Up Models and Database

#### Description
Create a SQLModel data model for books and configure a SQLite database file. Ensure your app creates tables automatically when the server starts.

#### Requirements
Completed program should:

- Define a `Book` model with fields for `id`, `title`, `author`, and `year`.
- Configure a SQLite database connection (for example, `books.db`).
- Create a reusable `get_session()` helper for database access.
- Create database tables during application startup.


### 🛠️	Build CRUD API Endpoints

#### Description
Implement API endpoints to create, read, update, and delete books using database sessions. Return clear JSON responses and useful error messages.

#### Requirements
Completed program should:

- Implement `POST /books` to add a new book.
- Implement `GET /books` to return all books.
- Implement `GET /books/{book_id}` to return a single book.
- Implement `PUT /books/{book_id}` to update an existing book.
- Implement `DELETE /books/{book_id}` to remove a book.
- Return a 404 response when `book_id` does not exist.
