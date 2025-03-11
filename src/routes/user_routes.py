from fastapi import APIRouter, Query
from typing import Annotated
from pydantic import BaseModel

router = APIRouter()

# Data validation
class User(BaseModel):
    name: str
    email: Annotated[str | None, Query(min_length = 3,max_length=60)] = None
    age: int

@router.get('/')
def index():
    return {'user': 'wilfred'}  

@router.post('/')
async def create(user: User):
    return {"name": user.name, "email" : user.email , "age" : user.age }