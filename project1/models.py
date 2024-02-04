DATABASE_URL='postgresql://postgres:macd1234@localhost:5432/Mac_ENGO551_Lab1'

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    isbn = Column(Integer)
    title = Column(String)
    author = Column(String)
    year = Column(Date)
    
    def __repr__(self):
        return "<Book(isbn= '{}', title='{}', author='{}', year={})>"\
                .format(self.isbn, self.title, self.author, self.year)
    

from sqlalchemy import create_engine

engine = create_engine(DATABASE_URL)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
s = Session()


s.add(Book)
s.commit()

s.close()