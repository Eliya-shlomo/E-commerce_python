from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker

## need to get user 
DATABASE_URL = "postgresql://user:password@localhost:5432/user_db"

engine = create_engine(DATABASE_URL)
SessionLoacl = sessionmaker(autocommit=False,autoFlash=False,bind=engine)
Base = declarative_base() 

def get_db():
    db = SessionLoacl()
    try:
        yield  db
    finally:
        db.close
    
