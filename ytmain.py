from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Book(BaseModel):
    name : str
    author : str
    year : int

@app.get('/')
def example():
    return {"data" : {"name" : "Steve"}}

# @app.get("/about")
# def about():
#     return {"author" : "Steve","age" : 22,}

@app.get('/about')
def about(limit : int = 10 ,published : bool = None,sort : Optional[str] = None):
    if(published):
        return {"data" : f"{limit} published books."}
    else:
        return {"data" : f"{limit} unplished books."}


@app.get("/about/secret")
def getSecret():
    return "Secret"

@app.get("/about/{id}")
def getBookById(id : int):
    return {"Id" : id}

@app.post("/about")
def createNewBook(book : Book):
    return {"name" : book.name,"author" : book.author, "year" : book.year}

