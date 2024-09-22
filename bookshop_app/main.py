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


# TODO: setup post endpoint with function to add book to inventory
# TODO: add functionality to update stock numbers also
@shop_app.post("/book", )  # add response_model for response
def create_book(book: schemas.StockBase, db: Session = Depends(get_db)):
    # not sure i need this key but lets keep it for now
    key = "".join(secrets.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(5))
    db_book = models.Stock(
        title=book.title, author=book.author,
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

# TODO: setup post endpoint to create orders and add these to an orders database
# TODO: add functionality to remove stock from inventory according to orders

# TODO: setup endpoint to mark orders as completed

# TODO: setup endpoint to view current orders and current stock