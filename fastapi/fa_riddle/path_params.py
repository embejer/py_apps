from fastapi import FastAPI
from typing import TypeVar
from enum import Enum


T = TypeVar("T")

class Position(str, Enum):
    father = 'Leo'
    mother = 'May'
    hubby = 'Em'
    wifey = 'Grace'

app = FastAPI()

@app.get("/items/{generic_id}")
async def read_item(generic_id: T):
    return {f'generic item_id {type(generic_id)}': generic_id}

@app.get("/items/{int_id}")
async def read_item(int_id: int):
    return {f'int item_id {type(int_id)}': int_id}

@app.get("/items/{str_id}")
async def read_item(str_id: str):
    return {f'str item_id {type(str_id)}': str_id}

@app.get("/items/{bool_id}")
async def read_item(bool_id: bool):
    return {f'str item_id {type(bool_id)}': bool_id}

'''
in path parameters ONLY int, str, float and boolean are working

seem Pydantic has an effect on boolean hints or type, it automatically gives True/False options => (type class is string)
'''

@app.get("/position/{position}")
async def read_item(position: Position):
    return {f'str item_id {type(position)} => {position.name}': position}

'''
from enum import Enum
class Sizes(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

values = [member.value for member in Sizes]
print(values)  # 👉️ [1, 2, 3]

names = [member.name for member in Sizes]
print(names)  # 👉️ ['SMALL', 'MEDIUM', 'LARGE']

'''