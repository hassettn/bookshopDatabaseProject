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


#why do it this way and not with sessionmaker?
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def random_key(len: int):
    key = "".join(secrets.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") for _ in range(len))
    return key

# TODO: add testing for database functionality


@shop_app.get("/")
def read_root():
    return "Welcome to my bookshop :)"


# TODO: add functionality to update stock numbers also
# endpoint to add a book to the stock table
@shop_app.post("/book")  # add response_model for response
def create_book(book: schemas.Stock, db: Session = Depends(get_db)):
    if crud.get_book_by_author_title(db=db, author=book.author, title=book.title,):
        return "book already exists"
    else:
        key = random_key(5)
        db_book = models.Stock(
            title=book.title,
            author=book.author,
            key=key,
            stock=book.stock,
            in_stock=bool(book.stock),
        )
        db.add(db_book)
        db.commit()
        db.refresh(db_book)
        return db_book


# TODO: add functionality to remove stock from inventory according to orders
# TODO: disallow zero quantity orders
# TODO: refine what information requested and returned
# endpoint to add an order to the orders table
@shop_app.post("/order")  # add response_model for response
def create_order(order: schemas.Orders, db: Session = Depends(get_db)):
    if book:=crud.get_book_by_author_title(db=db, author=order.author, title=order.title,):
        if book.stock < order.quantity:
            return "not enough books!"
        #add order details to order table
        key = random_key(5)
        db_order = models.Order(
            title=order.title,
            author=order.author,
            key=key,
            quantity=order.quantity,
            # complete=False,
        )
        db.add(db_order)
        db.commit()

        # to update stock levels in stock table
        db_book = (db.query(models.Stock)
                   .filter(models.Stock.author==order.author, models.Stock.title==order.title)
                   .first())
        setattr(db_book, 'stock', book.stock - order.quantity)
        db.commit()  # should i change db to session?
        # db.refresh(db_book)  # what does db.refresh do?

        db.refresh(db_order)

        return db_order
    else:
        return "book doesn't exist idiot"


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


@shop_app.post("/book/restock")
def restock_book(title, author, quantity:int, db: Session = Depends(get_db), ):
    #add a number of stock to a book listing which already exists
    db_book= crud.get_book_by_author_title(db=db, author=author, title=title, )
    if db_book:
        #then update the stock
        db_book.stock = int(db_book.stock) + quantity
        db_book.in_stock=bool(db_book.stock)
        db.commit()
        db.refresh(db_book)
        return db_book
    else:
        return "book does not yet exist,please add using /book endpoint"