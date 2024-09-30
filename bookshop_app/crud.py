# bookshop_app/crud.py
# create update delete

from sqlalchemy.orm import Session
from . import models, schemas

# TODO: move create-update-delete functionality here


def get_book_by_author_title(db: Session, author: str, title: str) -> models.Stock:
    # returns a book if it exists in the database, otherwise None
    return (
        db.query(models.Stock)
        .filter(models.Stock.author == author, models.Stock.title == title)
        .first()
    )
