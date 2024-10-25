import os
import uvicorn
from fastapi import FastAPI

import models
from database import SessionLocal, engine
from routers import auth, todos, admin, users

# to encrypt/hash passwords, install below packages.
# pip install passlib
# pip install bcrypt


# Python forms
# pip install python-multipart

# JWT - JSON Web Tokens
# pip install "python-jose[cryptography]"

# PostgreSQL Database Connector
# pip install psycopg2-binary

# Alembic - Database Migration Tool - Manage Schema changes and apply migrations
# pip install alembic
# Alembic commands:-
# alembic init <folder_name>    :   Initialize a new generic environment.
# alembic revision -m <message> :   Creates a new revision of the environment.
# alembiv upgrade <revision #>  :   Run our upgrade migration to our database.
# alembiv downgrade -1          :   Run our downgrade migration to our database.




app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)


if __name__ == "__main__":
    clear = lambda : os.system("clear")
    clear()
    uvicorn.run(app, host="0.0.0.0", port=33333)