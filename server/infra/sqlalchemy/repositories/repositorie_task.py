from sqlalchemy.orm import Session
from sqlalchemy import select, values
from server.infra.sqlalchemy.models import model_task
from server.schemas import schemas_task

class RepositorioTask:

    def __init__(self, db: Session):
        self.db = db

    def listar(self):
        tasks = self.db.query(model_task.Task).all()
        return tasks
    
    def criar(self, task: schemas_task.Task):
        db_task = model_task.Task(name = task.name, isDone = task.isDone) 
        self.db.add(db_task)
        self.db.commit()
        self.db.refresh(db_task)
        return db_task

