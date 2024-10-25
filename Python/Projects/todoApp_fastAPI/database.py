from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base



# To Use Inbuilt SQL-LITE-DB
# SQLALCHEMY_DATABASE_URL = "sqlite:///Data\\app.db"
# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})

# PostgreSQL Host Configuration = "postgresql://user_name:password@server_address/database_name"
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:pass1234@localhost/application"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

