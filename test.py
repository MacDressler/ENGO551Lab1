import os
import csv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker

print(os.getenv("DATABASE_URL"))