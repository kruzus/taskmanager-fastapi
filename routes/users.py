from fastapi import APIRouter, Depends, HTTPException, status




USERS_ROUTER = APIRouter(
    prefix="/users",
    tags=["users"]
)

@USERS_ROUTER.get("/")
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]