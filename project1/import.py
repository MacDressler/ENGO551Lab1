#My import file.
#Feb 4 2024

import os
import csv
from sqlalchemy import create_engine, text

from sqlalchemy.orm import scoped_session, sessionmaker

engine =create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def add_books():
    """Add Books to database"""
    global db
    with open('books.csv','r') as file:
        books = csv.reader(file)
        next(books) # You have to skip the first line

        for isbn, title, author, year in books:
            db.execute(text("insert into books (isbn, title, author, year) values (:isbn, :title, :author, :year);"),{'isbn':isbn, 'title':title, 'author':author, 'year':int(year)})
            
        db.commit()
        file.close()
        print("Uploading Finished")
def create_user_table():
    """This function creates the user table. I call it below but have it commented out because I don't need to recreate it over and over"""
    global db
    create_user_table = text("""
    CREATE TABLE users (
          id SERIAL PRIMARY KEY,
          username VARCHAR NOT NULL unique,
          password VARCHAR NOT NULL
      );
    """)
    db.execute(create_user_table)
    db.commit()
    print("User Table Created")


def create_book_table():
    """This function creates the book table but it is also commented out."""
    global db
    create_book_table = text("""
    CREATE TABLE books (
          id SERIAL PRIMARY KEY,
          isbn VARCHAR NOT NULL,
          title VARCHAR NOT NULL,
          author VARCHAR NOT NULL,
          year INTEGER NOT NULL
      );
    """)
    db.execute(create_book_table)
    db.commit()
    print("Book Table Created")

def create_review_table():
    """This function creates the review table but it is also commented out."""
    global db
    create_book_table = text("""
    CREATE TABLE review (
          id SERIAL PRIMARY KEY,
          username VARCHAR NOT NULL,
          review VARCHAR NOT NULL,
          rating INTEGER NOT NULL,
          book_id INT NOT NULL
      );
    """)
    db.execute(create_book_table)
    db.commit()
    print("Review Table Created")


if __name__ == '__main__':
    #create_user_table()
    create_book_table()
    #create_review_table()
    add_books()
