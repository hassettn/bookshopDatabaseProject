# bookshop_app/schemas.py

from pydantic import BaseModel


class StockBase(BaseModel):
    title: str
    author: str


# TODO: answer and remove questions!
# why are these built on top of each other like this??
# what does class Config: do??
# if a future employer is reading through every detail of my commits - don't you have anything better to do??
# should orders and stock be built from the same base schema?


class Stock(StockBase):
    # in_stock: bool
    # searches: int
    class Config:
        orm_mode = True


"""class StockInfo(Stock):
    url: str
    admin_url: str"""


class OrdersBase(BaseModel):
    title: str
    author: str


class Orders(OrdersBase):
    # quantity: int
    class Config:
        orm_mode = True
