# bookshop_app/main.py

import validators
from fastapi import Depends, FastAPI, HTTPException, Request

from sqlalchemy.orm import Session

from . import models, schemas, crud
from .database import SessionLocal, engine

# TODO: setup FastAPI

# TODO: setup database
models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# TODO: add testing for database functionality

# TODO: setup post endpoint with function to add book to inventory
# TODO: add functionality to update stock numbers also

# TODO: setup post endpoint to create orders and add these to an orders database
# TODO: add functionality to remove stock from inventory according to orders

# TODO: setup endpoint to mark orders as completed

# TODO: setup endpoint to view current orders and current stock