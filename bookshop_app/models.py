# bookshop_app/models.py

from sqlalchemy import Boolean, Column, Integer, String
from .database import Base


class Stock(Base):
    __tablename__ = "stock"

    id = Column(Integer, primary_key=True)
    # do I need a key as well as an id?
    key = Column(String, unique=True, index=True)
    title = Column(String, unique=False, index=True)
    author = Column(String, unique=False, index=True)
    stock = Column(Integer, default=0)
    in_stock = Column(Boolean, default=True)
    searches = Column(Integer, default=0)


# convention to give class sing. name and table plur. name
class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    # do I need a key as well as an id?
    key = Column(String, unique=True, index=True)
    title = Column(String, unique=False, index=True)
    author = Column(String, unique=False, index=True)
    quantity = Column(Integer, default=0)
    customer = Column(String, unique=False, index=True)
    # complete = Column(Boolean, default=False)


# TODO: add table for customers
