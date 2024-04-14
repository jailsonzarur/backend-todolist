from fastapi import FastAPI, Depends
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from server.schemas.schemas_task import Task
from server.infra.sqlalchemy.config.database import criar_db, get_db
from sqlalchemy.orm import Session
from server.infra.sqlalchemy.repositories.repositorie_task import RepositorioTask
from server.routers import routers_task

origins = ['http://127.0.0.1:8000/']

middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )
]


app = FastAPI()

#TASK ROUTERS
app.include_router(routers_task.router)


