from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

books = [
  {"id": 2,  "title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
  {"id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
  {"id": 4, "title": "One Hundred Years of Solitude", "author": "Gabriel Garcia Marquez","year": 1967},
  {"id": 5, "title": "Pride and Prejudice", "author": "Jane Austen","year": 1813}
]


@app.get("/books")
def getBook(author : str = None, year :int = None):
    for book in books:
        result = books
        if author == book["author"]:
            result = book
        if year == book["year"]:
            result = book
    return result

@app.get("/books/{book_id}")
def get_single_book(book_id: Optional[int] = None):
    for book in books:
        if book["id"] == book_id:
            return book
    return {"message": "Book not found"}

class Book(BaseModel):
    title : str
    author : str
    year : int

@app.post("/books")
def create_book (book : Book ):
    newBook = {
        "id" : 6,
        "title" : book.title,
        "author" : book.author,
        "year" : book.year}
    books.append(newBook)
    return { "message" : "Book created successfully" , "Book" : newBook}

