from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Books API Starter")


class BookInput(BaseModel):
    title: str
    author: str
    year: int


# In-memory data store for this assignment
books = [
    {"id": 1, "title": "Clean Code", "author": "Robert C. Martin", "year": 2008},
    {"id": 2, "title": "The Pragmatic Programmer", "author": "Andrew Hunt", "year": 1999},
]


@app.get("/")
def read_root():
    # Task 1: return a short welcome message for the API homepage.
    return {"message": "Welcome to the Books API"}


@app.get("/books")
def get_books():
    # Task 1: return all books.
    return books


@app.get("/books/{book_id}")
def get_book(book_id: int):
    # Task 1: return a single book by id or raise 404.
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@app.post("/books")
def create_book(book: BookInput):
    # Task 2: create a new book using validated input data.
    new_id = max((item["id"] for item in books), default=0) + 1
    new_book = {"id": new_id, **book.model_dump()}
    books.append(new_book)
    return new_book


@app.put("/books/{book_id}")
def update_book(book_id: int, book: BookInput):
    # Task 2: update an existing book or raise 404.
    for index, existing_book in enumerate(books):
        if existing_book["id"] == book_id:
            updated_book = {"id": book_id, **book.model_dump()}
            books[index] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found")
