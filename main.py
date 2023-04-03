from typing import Union
import uvicorn

from routes import users, tasks
# from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

app = FastAPI()

# from database import engine, SessionLocal, Base
# Base.metadata.create_all(bind=engine)

# origins = [
#     "http://localhost",
#     "http://localhost:8080",
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

app.include_router(users.USERS_ROUTER, prefix="/api")
app.include_router(tasks.TASKS_ROUTER, prefix="/api")


@app.get("/")
async def home():
    return {
        "msg": "This is home"
    }



if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=5000, log_level="warning")