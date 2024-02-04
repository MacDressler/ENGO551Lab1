#This file will do the importing of the list of books.

import os
import csv
from sqlalchemy import create_engine, text

from sqlalchemy.orm import scoped_session, sessionmaker

engine =create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))



def main():
    b = open('books.csv')
    reader = csv.reader(b)
    next(reader)
    for isbn,title,author,year in reader:
        db.execute(text("INSERT INTO books (ISBN, Title, Author, Year) VALUES (:isbn, :title, :author, :year)"),
                   {"isbn": int(isbn), "title": title, "author": author, "year": int(year)})
        print(f"added book called {title} with ISBN Number {isbn}")

    db.commit

if __name__ == "__main__":
    main()