
from fastapi import FastAPI , HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()
books = [
  {"id": 2,  "title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
  {"id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
  {"id": 4, "title": "One Hundred Years of Solitude", "author": "Gabriel Garcia Marquez","year": 1967},
  {"id": 5, "title": "Pride and Prejudice", "author": "Jane Austen","year": 1813}
]
@app.delete('/books/{book_id}')
def delete_book(book_id : int):
 # 0 : afjd
 # 1 : adf
  for i , book in enumerate(books):
    if book["id"] == book_id:
      deleted_book = books.pop(i)
      return {"message" : "Book deleted successfully" , "book" : deleted_book}
    
  
  raise HTTPException(status_code=404 , detail= "Book not found")