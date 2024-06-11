from datetime import datetime
from enum import Enum
from typing import List, Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(
    title='Traiding'
)


fake_users = [
    {'id': 1, 'role': 'admin', 'name': 'Bob'},
    {'id': 2, 'role': 'trader', 'name': 'Cris'},
    {'id': 3, 'role': 'client', 'name': 'Rock'},
]


class DegreeType(Enum):
    newbie = 'newbie'
    expert = 'expert'


class Degree(BaseModel):
    id: int
    created_at: datetime
    type_degree: DegreeType


class User(BaseModel):
    id: int
    role: int
    name: str
    degree: Optional[List[Degree]] = []




@app.get('/users/{user_id}', response_model=List[User])
def get_user(user_id: int):
    return [user for user in fake_users if user.get('id') == user_id]


fake_trades = [
    {'id': 1, 'user_id': 1, 'currency': 'BTC', 'side': 'buy', 'price': 123, 'amount': 2.12},
    {'id': 2, 'user_id': 1, 'currency': 'BTC', 'side': 'sell', 'price': 125, 'amount': 2.12},
]


class Trade(BaseModel):
    id: int
    user_id: int
    currency: str = Field(max_length=5)
    side: str
    price: float = Field(ge=0)
    amount: float




@app.post('trades')
def add_trades(trades: List[Trade]):
    fake_trades.extend(trades)
    return {'status': 200, 'data': fake_trades}
