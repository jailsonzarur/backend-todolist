from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#SQLALCHEMY_DATABASE_URL = "sqlite:///./app_task.db"
SQLALCHEMY_DATABASE_URL = "postgresql://backend_todolist_db_user:sVFbYqCAJ5Dyl2povQCl7yMYyYHWB6d0@dpg-coe0us20si5c73990rq0-a.oregon-postgres.render.com/backend_todolist_db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def criar_db():
    Base.metadata.create_all(bind=engine)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
