from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.models import user
from src.auth.schemas import UserRead
from src.database import get_async_session

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)
