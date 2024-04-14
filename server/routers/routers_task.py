from fastapi import FastAPI, Depends, APIRouter, status
from server.schemas.schemas_task import Task
from server.infra.sqlalchemy.config.database import criar_db, get_db
from sqlalchemy.orm import Session
from server.infra.sqlalchemy.repositories.repositorie_task import RepositorioTask

router = APIRouter()

@router.post('/task', status_code= status.HTTP_201_CREATED)
def createtask(task: Task, db: Session = Depends(get_db)):
    task_criada = RepositorioTask(db).criar(task)
    return task_criada

@router.get('/task')
def alltasks(db: Session = Depends(get_db)):
    tasks = RepositorioTask(db).listar()
    return tasks

@router.get('/task/{id}')
def singletask(id: int, db: Session = Depends(get_db)):
    task = RepositorioTask(db).obtain(id)
    return task

@router.put('/task/{id}')
def updatetask(id: int, db: Session = Depends(get_db)):
    return RepositorioTask(db).update(id)

@router.delete('/task/{id}')
def deletetask(id: int, db: Session = Depends(get_db)):
    return RepositorioTask(db).delete(id)

