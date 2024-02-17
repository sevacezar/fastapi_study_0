from fastapi import FastAPI
from database import create_tables, drop_tables
from contextlib import asynccontextmanager

from router import router as tasks_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await drop_tables()
    print('БД очищена')
    await create_tables()
    print('БД готова к работе')
    yield
    print('Выключение')


app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)