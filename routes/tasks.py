from fastapi import APIRouter, Depends, HTTPException, status




TASKS_ROUTER = APIRouter(
    prefix="/tasks",
    tags=["tasks"]
)

@TASKS_ROUTER.get("/")
async def read_task():
    return {"hello": "tasks"}