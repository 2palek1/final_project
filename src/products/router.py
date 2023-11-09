from fastapi import APIRouter, Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.utils import get_user_db
from productscheme import ProductSchema
from src.auth.models import User
from src.database import get_async_session

router = APIRouter()

async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)

database = []

@router.post("/products/create/", response_model= ProductSchema)
async def create_product(product: ProductSchema, user_db: SQLAlchemyUserDatabase = Depends(get_user_db)):
    current_user = await user_db.get_by_id(1)
    product_info = product.dict()
    product_info["user_id"] = current_user.id
    database.append(product_info)
    return product


@router.get("/products/{product_id}", response_model=ProductSchema)
async def get_product(product_id: int):
    return database[product_id - 1]