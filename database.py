from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session

DATABASE_URL = 'postgresql://postgres:1@localhost/bookdb'

engine = create_engine(DATABASE_URL, echo=True)

Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)