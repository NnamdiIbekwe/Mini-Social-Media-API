import os
from dotenv import load_dotenv
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker 
from sqlalchemy import create_engine


load_dotenv()

engine = create_engine(
    os.getenv("DATABASE_URL"),
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()