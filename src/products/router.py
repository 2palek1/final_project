from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.products.models import product_item, product

from src.products.schemas import ProductSchema, ProductItemSchema


router = APIRouter(
    prefix="/products",
    tags=["product"]
)


@router.get("/{product_id}")
async def get_product(product_id: int, session: AsyncSession = Depends(get_async_session)):
    try:
        stmt = select(product_item).where(product_item.c.id == product_id)
        result = await session.execute(stmt)
        product_data = result.fetchone()
        return {
            "status": "success",
            "data": product_data,
            "details": None
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": str(e)
        })


@router.post("/create_product")
async def create_product(new_product: ProductSchema, new_product_item: ProductItemSchema, session: AsyncSession = Depends(get_async_session)):
    try:
        stmt = insert(product).values(**new_product.dict())
        stmt_item = insert(product_item).values(**new_product_item.dict())
        await session.execute(stmt)
        await session.commit()
        await session.execute(stmt_item)
        await session.commit()
        return {
            "status": "success",
            "data": [new_product, new_product_item],
            "details": None
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": str(e)
        })


@router.post("/create_product_item")
async def create_product_item(new_product_item: ProductItemSchema, session: AsyncSession = Depends(get_async_session)):
    try:
        stmt = insert(product_item).values(**new_product_item.dict())
        await session.execute(stmt)
        await session.commit()
        return {
            "status": "success",
            "data": new_product_item,
            "details": None
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": str(e)
         })


