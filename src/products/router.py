from fastapi import APIRouter, Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.utils import get_user_db
from src.database import get_async_session
from src.products.models import product_item, product
from src.products.schemas import ProductSchema, ProductItemSchema

router = APIRouter(
    prefix="/products",
    tags=["product"]
)


@router.post("/")
async def create_product(new_product: ProductSchema, new_product_item: ProductItemSchema, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(product).values(**new_product.dict())
    stmt_item = insert(product_item).values(**new_product_item.dict())
    await session.execute(stmt)
    await session.commit()
    await session.execute(stmt_item)
    await session.commit()
    return {"status": 200, "new_product": new_product, "new_product_item": new_product_item}


# @router.post("/")
# async def create_product_item(new_product_item: ProductItemSchema, session: AsyncSession = Depends(get_async_session)):
#     try:
#         stmt = insert(product_item).values(**new_product_item.dict())
#         await session.execute(stmt)
#         return new_product_item
#     except Exception as error:
#         return error


@router.get("/{product_id}", response_model=ProductSchema)
async def get_product(product_id: int,session: AsyncSession = Depends(get_async_session)):
    stmt = select(product_item).where(product_item.c.id == product_id)
    await session.execute(stmt)
