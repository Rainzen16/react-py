from fastapi import APIRouter
from services.users import UserService

router = APIRouter()

userService = UserService()

@router.get("/", tags=["Default"])
async def get_all_users():
    return await userService.get_all_users()
