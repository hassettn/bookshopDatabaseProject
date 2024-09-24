# bookshop_app/main.py

from fastapi import Depends, FastAPI, HTTPException, Request
import secrets

from sqlalchemy.orm import Session

from . import models, schemas, crud
from .database import SessionLocal, engine

# setup FastAPI
shop_app = FastAPI()

# setup database
models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# TODO: add testing for database functionality


@shop_app.get("/")
def read_root():
    return "Welcome to my bookshop :)"


# TODO: add functionality to update stock numbers also
# endpoint to add a book to the stock table
@shop_app.post("/book", )  # add response_model for response
def create_book(book: schemas.StockBase, db: Session = Depends(get_db)):
    # not sure whether I need this key but let's keep it for now
    key = "".join(secrets.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(5))
    db_book = models.Stock(
        title=book.title, author=book.author, key=key
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


# TODO: add functionality to remove stock from inventory according to orders
# TODO: refine what information requested and returned
# TODO: unite tables in base model and refine function
# endpoint to add an order to the orders table
@shop_app.post("/order", )  # add response_model for response
def create_order(order: schemas.OrdersBase, db: Session = Depends(get_db)):
    # not sure that I need this key but let's keep it for now
    key = "".join(secrets.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(5))
    db_order = models.Order(
        title=order.title, author=order.author, key=key,
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


# endpoint to view current stock
# TODO: add response_model
@shop_app.get("/current_stock", )
def get_stock(db: Session = Depends(get_db), ):
    # needs the .all() tag to work!
    return db.query(models.Stock).all()


# TODO: add filters for uncompleted orders
# TODO:add response_model
# endpoint to view all orders
@shop_app.get("/orders", )
def get_orders(db: Session = Depends(get_db), ):
    # needs the .all() tag to work!
    return db.query(models.Order).all()

