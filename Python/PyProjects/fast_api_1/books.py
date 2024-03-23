import json
from fastapi import FastAPI

app = FastAPI()


def get_data():
    with open("data.json", "r") as file:
        data = json.load(file)
    return data


@app.get("/")
@app.get("/index")
async def first_api():
    print(get_data())

    print(get_data()[0]["title"])
    print(get_data()[1]["author"])

    return {"message" : "Hello Learner!!"}


@app.get("/books")
async def read_books():
    return get_data()


@app.get("/books/{title}")
async def read_book(title: str):
    for book in get_data():
        if book.get('title').casefold() == title.casefold():
            return book
        

@app.get("/books/")
async def read_by_category(category: str):
    books_to_return = []

    for book in get_data():
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    
    return books_to_return


@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in get_data():
        if book.get('author').casefold() == book_author.casefold() and \
                book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return
            
        
        
