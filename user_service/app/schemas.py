from pydantic import BaseModel, EmialStr

class UserBase(BaseModel):
    username : str
    email = EmialStr

class UserCreate(BaseModel):
    password : str

class UserResoponse(BaseModel):
    id : int


    class config:
        orm_mode = True

