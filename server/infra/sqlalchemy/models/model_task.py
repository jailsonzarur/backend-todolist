from server.infra.sqlalchemy.config.database import Base
from sqlalchemy import Column, Integer, String, Boolean

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String)
    isDone = Column(Boolean)