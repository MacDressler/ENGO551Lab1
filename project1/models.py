DATABASE_URL='postgresql://postgres:macd1234@localhost:5432/Mac_ENGO551_Lab1'

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


from sqlalchemy import create_engine

engine = create_engine(DATABASE_URL)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
s = Session()



s.commit()

s.close()