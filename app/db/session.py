from sqlalchemy.orm import sessionmaker
from app.db.base import engine, Base



sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

