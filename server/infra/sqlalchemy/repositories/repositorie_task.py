from sqlalchemy.orm import Session
from sqlalchemy import select, values, exists, insert, update
from server.infra.sqlalchemy.models import model_task
from server.schemas import schemas_task

class RepositorioTask:

    def __init__(self, db: Session):
        self.db = db

    def listar(self):
        tasks = self.db.query(model_task.Task).all()
        return tasks

    def criar(self, task: schemas_task.Task):
        stmt = select(model_task.Task).filter_by(name = task.name)
        possiveltask = self.db.execute(stmt).scalars().all()
        if possiveltask:
            return {"Message": "This task already exists."}
        db_task = model_task.Task(name = task.name, isDone = task.isDone) 
        self.db.add(db_task)
        self.db.commit()
        self.db.refresh(db_task)
        return db_task

    def obtain(self, idtask: int):
        task = self.db.query(model_task.Task).get(idtask)
        return task