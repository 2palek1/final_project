from fastapi import APIRouter, Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase

from src.auth.utils import get_user_db
from src.products.schemas import ProductSchema

router = APIRouter(
    prefix="/products",
    tags=["product"]
)

database = []


@router.post("/create", response_model=ProductSchema)
async def create_product(product: ProductSchema, user_db: SQLAlchemyUserDatabase = Depends(get_user_db)):
    current_user = await user_db.get_by_id(1)
    product_info = product.dict()
    product_info["user_id"] = current_user.id
    database.append(product_info)
    return product


@router.get("/{product_id}", response_model=ProductSchema)
async def get_product(product_id: int):
    return database[product_id - 1]
