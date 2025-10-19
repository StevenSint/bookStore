from fastapi import FastAPI
from typing import Optional

app = FastAPI()

books = [
    {"id": 1, "title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    {"id": 2, "title": "1984", "author": "George Orwell", "year": 1949},
    {"id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
    {"id": 4, "title": "Pride and Prejudice", "author": "Jane Austen", "year": 1813},
    {"id": 5, "title": "The Catcher in the Rye", "author": "J.D. Salinger", "year": 1951}
]

@app.get('/')
def read_root():
    return {"Hello": "World"}

@app.get("/books/{book_id}")
def get_single_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    return {"message": "Book not found"}

# @app.get("/books")
# def get_books(author: Optional[str] = None, year: Optional[int] = None):
#     result = []
    
#     for book in books:
#         # Check author filter
#         if author and author.lower() not in book["author"].lower():
#             continue
            
#         # Check year filter  
#         if year is not None and book["year"] != year:
#             continue
            
#         result.append(book)
    
#     return {
#         "filters": {"author": author, "year": year},
#         "count": len(result),
#         "books": result
#     }

@app.post("/books")
def create_book (book : Book ):
    new_book = {
        "id" : 6,
        "title" : book titile,
        "author" : book.author,
        "year" : book.year}
        books.append(new_book)
I
    return { "message" : "Book created successfully" , "Book" : new_book}