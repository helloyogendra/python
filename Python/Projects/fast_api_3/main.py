import uvicorn
from fastapi import FastAPI, Body

# if installed using - 'pip install fastapi- and 'pip install "uvicorn[standard]"',     # Use below command to run
# uvicorn main:app --reload                                                             # Here main is the name of the the file

# if installed using - 'pip install "fastapi[standard]"',                               # Use belo command to run
# fastapi dev books.py                                                                  # Here books is the name of the the file

app = FastAPI()


books = [
    {'title' : 'Title One', 'author': 'A One', 'category': 'science'},
    {'title' : 'Title Two', 'author': 'A Two', 'category': 'science'},
    {'title' : 'Title Three', 'author': 'A Three', 'category': 'math'},
    {'title' : 'Title Four', 'author': 'A Four', 'category': 'history'}
]

# Get Request Method

# http://127.0.0.1:8000
@app.get("/")
async def first():
    return {"message" : "Hello"}


# Path Parameters
# http://127.0.0.1:8000/books
@app.get("/books")
async def get_all_books():
    print("//books")
    return books

# Path Parameters
# http://127.0.0.1:8000/books/Title%20One
@app.get("/books/{title}")
async def find_a_book(title: str):
    print("//books//title ", title)
    for book in books:
        if book.get('title').casefold() == title.casefold():
            return book


# Query Parameters 
# http://127.0.0.1:8000/books/?category=science
@app.get("/books/")
async def find_by_category(category: str):
    
    lst = []
    for book in books:
        if book.get('category').casefold() == category.casefold():
            lst.append(book)
    return lst


# Query Parameters
# Syntax of URL =   http://127.0.0.1:8000/books/author/?category=science
# Actual URL =      http://127.0.0.1:8000/books/a%20one/?category=science
@app.get("/books/{author}/")
async def find_by_category(author: str, category: str):
    lst = []
    for book in books:
        if book.get('author').casefold() == author.casefold() and \
                book.get('category').casefold() == category.casefold():
            lst.append(book)
    return lst




# Post Request Method 

@app.post("/books/create_book")
async def create_book(new_book=Body()):
    books.append(new_book)


# Put Request Method

@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(books)):
        if books[i].get('title').casefold() == updated_book.get('title').casefold():
            books[i] = updated_book

# Delete Request Method
@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(books)):
        if books[i].get("title").casefold() == book_title.casefold():
            books.pop(i)
            break


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=33333)