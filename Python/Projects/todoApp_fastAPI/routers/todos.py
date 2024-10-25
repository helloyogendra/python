import uvicorn
from typing import Annotated
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field
from fastapi import Depends, APIRouter, HTTPException, status, Path

from models import Todos
from database import SessionLocal, engine
from .auth import get_current_user


router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]


class ToDoRequest(BaseModel):
    title: str = Field(min_length=3)
    description: str = Field(min_length=3, )
    priority: int
    complete: bool

    

@router.get("/", status_code=status.HTTP_200_OK)
async def read_all(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication Failed")
    
    return db.query(Todos).filter(Todos.owner_id == user.get('id')).all()


@router.get("/todo/{id}", status_code=status.HTTP_200_OK)
async def get_todo_by_id(user: user_dependency, db: db_dependency, id: int = Path(gt = 0)):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication Failed")
    
    todo_model = db.query(Todos).filter(Todos.id == id).filter(Todos.owner_id == user.get('id')).first()
                                        
    if todo_model:
        return todo_model
    raise HTTPException(status_code=404, detail='Todo not found')

@router.post("/todo", status_code=status.HTTP_201_CREATED)
async def create_todo(user: user_dependency, db:db_dependency, todo_request: ToDoRequest):

    if user is None:
        raise HTTPException(status_code=401, detail="Authentication Failed")

    todo_model = Todos(**todo_request.model_dump(), owner_id=user.get('id'))

    db.add(todo_model)
    db.commit()

@router.put("/todo/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_todos(user: user_dependency, db: db_dependency, todo_request: ToDoRequest, id: int= Path(gt = 0)):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication Failed")
    
    todo_model = db.query(Todos).filter(Todos.id == id) \
                                .filter(Todos.owner_id == user.get('id')).first()

    if not todo_model:
        raise HTTPException(status_code=404, detail="todo not found")

    todo_model.title = todo_request.title
    todo_model.description = todo_request.description
    todo_model.priority = todo_request.priority
    todo_model.complete = todo_request.complete

    db.add(todo_model)
    db.commit()

@router.delete("/todo/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def deleted_todos(user: user_dependency, db: db_dependency, id: int = Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication Failed")
    
    model = db.query(Todos).filter(Todos.id == id) \
                            .filter(Todos.owner_id == user.id).first()

    if not model:
        raise HTTPException(status_code=404, detail="todo details not found")
    
    db.query(Todos).filter(Todos.id == id).filter(Todos.owner_id == user.id).delete()
    db.commit()
    



if __name__ == "__main__":
    uvicorn.run(router, host="0.0.0.0", port=33333)