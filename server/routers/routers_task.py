from fastapi import FastAPI, Depends, APIRouter, status
from server.schemas.schemas_task import Task
from server.infra.sqlalchemy.config.database import criar_db, get_db
from sqlalchemy.orm import Session
from server.infra.sqlalchemy.repositories.repositorie_task import RepositorioTask

router = APIRouter()

@router.get('/')
def hello():
    return {"Message": "Hello Izaias!"}

@router.post('/tasks', status_code= status.HTTP_201_CREATED)
def createtask(task: Task, db: Session = Depends(get_db)):
    task_criada = RepositorioTask(db).criar(task)
    return task_criada

@router.get('/tasks')
def alltasks(db: Session = Depends(get_db)):
    tasks = RepositorioTask(db).listar()
    return tasks

@router.get('/tasks/{id}')
def singletask(id: int, db: Session = Depends(get_db)):
    task = RepositorioTask(db).obtain(id)
    return task

@router.put('/tasks/{id}')
def updatetask(id: int, db: Session = Depends(get_db)):
    return RepositorioTask(db).update(id)

@router.delete('/tasks/{id}')
def deletetask(id: int, db: Session = Depends(get_db)):
    return RepositorioTask(db).delete(id)

