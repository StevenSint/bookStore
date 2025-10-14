from fastapi import FastAPI

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
    return {"Hello" : "World"}\

# get retrive all books
@app.get('/books')
def getAllBooks():
    return books

# get retrive single book
@app.get("/books/{book_id}")
def get_single_book(book_id : int):

    #Get a specific book by ID (path parameter)
    for book in books:
        if book["id"] == book_id:
            return book
    
    return {"message" : "Book not found"}

# Get Retrive books by filtering using query parameters
@app.get("/books")
def getBooks(author : str | None, year : int | None):

    filtered_books = books

    if author :
        return {"author" : author}

    if year:
        return {"year" : year}

    return {"message" : "Not found"}
