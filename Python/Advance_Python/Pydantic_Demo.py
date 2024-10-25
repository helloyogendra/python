from datetime import datetime
from pydantic import BaseModel, PositiveInt, ValidationError

# Example-1

class User(BaseModel):
    id: int  
    name: str = 'John Doe'  
    signup_ts: datetime | None  
    tastes: dict[str, PositiveInt]  


external_data = {
    'id': 123,
    'signup_ts': '2019-06-01 12:22',  
    'tastes': {
        'wine': 9,
        b'cheese': 7,  
        'cabbage': '1',  
    },
}

user = User(**external_data)  

print(user.id)  
print(user.model_dump())  
print()

# Example-2

class User1(BaseModel):
    id: int
    name: str = 'John Doe'
    signup_ts: datetime | None
    tastes: dict[str, PositiveInt]

external_data1 = { 
    'id': '101',               # Exception will be thrown because of this line but '101' will be fine
    'name': 'Tom', 
    'signup_ts': None, 
    'tastes': {} 
    }  

try:
    user1 = User1(**external_data1)  
    #user1.age = 38                      # this is not allowed, Exception will be thrown 
except ValidationError as e:
    print(f"Exception : \n{e.errors()}")
except Exception as ex:
    print(ex)
else:
    print(user1.id)  
    print(user1.model_dump())
    print(user1.age)
 