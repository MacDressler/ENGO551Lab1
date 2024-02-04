import os
import csv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker

print(os.getenv("DATABASE_URL"))
DATABASE_URL = os.getenv("DATABASE_URL")
from sqlalchemy import create_engine, inspect
e = create_engine(os.getenv("DATABASE_URL"))
insp = inspect(e)
insp.default_schema_name

print(insp.default_schema_name)

from sqlalchemy import create_engine

engine = create_engine(DATABASE_URL)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date

Base = declarative_base()

Base.metadata.create_all(engine)