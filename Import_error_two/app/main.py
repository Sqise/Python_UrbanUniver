from fastapi import FastAPI
from routers import task, user
#from .backend.db import create_db_and_tables, drop_db_and_tables, print_create_table_sql

app = FastAPI()

app.include_router(task.router)
app.include_router(user.router)

@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}