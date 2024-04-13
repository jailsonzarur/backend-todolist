from fastapi import FastAPI, Depends
from server.schemas.schemas_task import Task
from server.infra.sqlalchemy.config.database import criar_db, get_db
from sqlalchemy.orm import Session
from server.infra.sqlalchemy.repositories.repositorie_task import RepositorioTask

criar_db()

app = FastAPI()

@app.post('/task')
def createtask(task: Task, db: Session = Depends(get_db)):
    task_criada = RepositorioTask(db).criar(task)
    return task_criada

@app.get('/task')
def alltasks(db: Session = Depends(get_db)):
    tasks = RepositorioTask(db).listar()
    return tasks

@app.get('/task/{id}')
def singletask(id: int, db: Session = Depends(get_db)):
    task = RepositorioTask(db).obtain(id)
    return task

@app.put('/task/{id}')
def updatetask(id: int, db: Session = Depends(get_db)):
    return RepositorioTask(db).update(id)

@app.delete('/task/{id}')
def deletetask(id: int, db: Session = Depends(get_db)):
    return RepositorioTask(db).delete(id)

