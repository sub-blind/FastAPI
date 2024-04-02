from pydantic import BaseModel
from typing import List
from typing import Optional


# schemas/item.py
# schemas/user.py
class ItemBase(BaseModel):
    title: str
    description: str


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class ItemCreate(ItemBase):
    pass


class ItemUpdate(ItemBase):
    title: str | None = None
    description: str | None = None


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    hashed_password: str


class UserUpdate(UserBase):
    email: str | None = None
    hashed_password: str | None = None  # python 3.10부터 추가된 기능입니다.


class User(UserBase):
    id: int
    items: List[Item]

    class Config:
        orm_mode = True
