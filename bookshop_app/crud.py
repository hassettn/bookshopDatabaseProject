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


def delete_book_by_id(db: Session, book_id: int, author: str, title: str):
    # deletes a book from the database given the id, if it exists in the database
    # requires author and title for added security
    return (
        db.query(models.Stock)
        .filter(models.Stock.id == book_id, models.Stock.author == author, models.Stock.title == title)
        .delete(synchronize_session="evaluate")
    )
