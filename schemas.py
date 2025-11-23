from pydantic import BaseModel

class StudentCreate(BaseModel):
    name: str
    age: int
    grade: str

class StudentOut(BaseModel):
    id: int
    name: str
    age: int
    grade: str

    class Config:
        orm_mode = True
