from datetime import datetime
from enum import Enum
from typing import List, Optional

from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import ValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI(
    title="Trading App"
)


@app.exception_handler(ValidationError)
async def validation_exception_handler(reqest: Request, exc: ValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors()})
    )


class Trade(BaseModel):
    id: int
    user_id: int
    currencym: str


class Type_degree(Enum):
    advanced = "advanced"
    intermediate = "intermediate"
    expert = "expert"


class Degree(BaseModel):
    id: int
    created_at: datetime
    type_degree: Type_degree


class User(BaseModel):
    id: int
    role: str
    name: str
    degree: Optional[list[Degree]] = []




user_list = [
    {"id": 1, "role": "tradaer", "name": ["Matt"], "degree": [
        {"id": 1, "created_at": "2023-12-31T23:59:59", "type_degree": "expert"}
    ]},
    {"id": 2, "role": "developer", "name": "John", "degree": [
        {"id": 2, "created_at": "2022-06-30T10:45:00", "type_degree": "intermediate"}
    ]},
    {"id": 3, "role": "tradaer", "name": "Sarah", "degree": [
        {"id": 3, "created_at": "2021-01-15T08:20:00", "type_degree": "advanced"}
    ]},
    {"id": 4, "role": "manager", "name": "David", "degree": [
        {"id": 4, "created_at": "2020-09-05T16:30:00", "type_degree": "intermediate"}
    ]},
    {"id": 5, "role": "developer", "name": "Emily", "degree": [
        {"id": 5, "created_at": "2022-11-20T12:15:00", "type_degree": "advanced"}
    ]},
    {"id": 6, "role": "tradaer", "name": "Mark", "degree": [
        {"id": 6, "created_at": "2019-05-10T19:40:00", "type_degree": "expert"}
    ]},
    {"id": 7, "role": "manager", "name": "Amy", "degree": [
        {"id": 7, "created_at": "2021-07-01T14:00:00", "type_degree": "advanced"}
    ]},
    {"id": 8, "role": "developer", "name": "Chris", "degree": [
        {"id": 8, "created_at": "2020-03-15T09:30:00", "type_degree": "intermediate"}
    ]},
    {"id": 9, "role": "tradaer", "name": "Karen", "degree": [
        {"id": 9, "created_at": "2022-02-28T17:50:00", "type_degree": "advanced"}
    ]},
    {"id": 10, "role": "manager", "name": "Tom", "degree": [
        {"id": 10, "created_at": "2019-11-10T13:25:00", "type_degree": "expert"}
    ]}
]

fake_trades = [
    {"id": 1, "user_id": 1, "currency": "BTC"},
    {"id": 2, "user_id": 3, "currency": "ЕTC"},
    {"id": 3, "user_id": 1, "currency": "SDY"},
    {"id": 4, "user_id": 4, "currency": "SDY55"},
    {"id": 5, "user_id": 1, "currency": "BTC"},
    {"id": 6, "user_id": 3, "currency": "ЕTC"},
    {"id": 7, "user_id": 1, "currency": "SDY"},
    {"id": 8, "user_id": 4, "currency": "SDY55"},
]


@app.get("/users/{user_id}", response_model=List[User])
def get_user(user_id: int):
    return [user for user in user_list if user.get("id") == user_id]


@app.get("/trades")
def get_trades(limit: int = 1, offset: int = 0):
    return fake_trades[offset:][:limit]


@app.post("/users/{user_id}")
def post_user(user_id: int, new_name: str):
    current_user = list(filter(
        lambda user: user.get("id") == user_id, user_list
    ))[0]
    current_user["name"] = new_name
    return {"status": 200, "data": current_user}


@app.post('/tredes')
def add_tredes(trades:list[Trade]):
    fake_trades.extend(trades)
    return {"status": 200, "data":trades}
