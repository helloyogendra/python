from typing import Optional
import uvicorn
from fastapi import Body, FastAPI, Path, Query, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    optional_field: str
    published_date: int

    def __init__(self, id, title, author, description, rating, optional_field, published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.optional_field = optional_field
        self.published_date = published_date

    def __str__(self):
        return f"Book Object : Id= {self.id}, Title= {self.title}, " \
            + f"Author= {self.author}, Description= {self.description}, Rating= {self.rating}, Optional Field= {self.optional_field}"


class BookRequest(BaseModel):
    id: int = Field()
    title: str = Field(min_length=3, max_length=15)
    author: str = Field(min_length=3, max_length=15)
    description: str = Field(min_length=3, max_length=25)
    rating: int = Field(gt=0, lt=6)
    optional_field: Optional[str] = Field(description='Optional_Field is optional', default="Empty String")
    published_date: int = Field(gt=1999, lt=2024)

    # define default schema model
    class Config:
        json_schema_extra = {
            "exmaple" : {
                "id" : 1,
                "title" : "A new book",
                "author" : "A Developer",
                "description": "Fill with new description",
                "rating": 5,
                "published_date": 2029
            }
        }
    


# Optional Fields need to be mentioned explictly, be default a field is mandatory


BOOKS = [
            Book(1001, "Python", "Matt", "Programming", 5, "", 2018), 
            Book(1002, "Graphical", "Maxx", "Interface", 5, "", 2017),
            Book(1003, "Computer", "John", "Basic", 4, "", 2021),
            Book(1004, "PandasPro","Tom", "Data", 4, "", 2021),
            Book(1005, "PySpark", "Matt", "Data", 3, "", 2023),
            Book (1006, "Database", "Maxx", "SQL", 5, "", 2022),
        ]



@app.get("/", status_code=status.HTTP_200_OK)
async def get_all_books():
    return BOOKS

@app.get("/error")
async def get_error():
    raise Exception("Server Exception : 5005")


# Path Parameters with Path validation also added, book_id must be > 0
#
@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
async def get_book_by_id(book_id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail='Item not found')



# Query Parameter with Query validation also added, rating must be > 0 and < 6
# http://127.0.0.1:44444/books/?rating=5

@app.get("/books/")
async def get_book_by_rating(rating: int= Query(gt=0, lt=6), status_code=status.HTTP_200_OK):
    result = []
    for book in BOOKS:
        if book.rating == rating:
            result.append(book)
    return result


#Query Parameter with Query validation also added, published_date must be > 2001 and < 2025
@app.get("/books/publish/")
async def get_by_publish_date(published_date: int = Query(gt=2001, lt=2025), status_code=status.HTTP_200_OK):
    result = []
    for book in BOOKS:
        if book.published_date == published_date:
            result.append(book)
    return result



@app.post("/create_book", status_code=status.HTTP_201_CREATED)
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())

    print(type(new_book))
    print(new_book)
    new_book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1

    print(new_book)
    BOOKS.append(new_book)
    # BOOKS.append(find_book_id(new_book))



@app.put("/books/update_book", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book: BookRequest):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book
            book_changed = True
    if not book_changed:
        raise HTTPException(404, 'item not found')



# Path Parameters with Path validation also added, book_id must be > 0
@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int = Path(gt=0)):
    book_changed = False
    for i in range (len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            book_changed = True
            break
    
    if not book_changed:
        raise HTTPException(404, 'item not found')

    

def find_book_id(book: Book):
    if len(BOOKS) > 0:
        book.id = BOOKS[-1].id + 1
    else:
        book.id = 1
    return book



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=44444)