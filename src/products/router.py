from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.products.models import product_item, product_category

from src.products.schemas import ProductItemSchema
from src.products.utils import get_product_dict

router = APIRouter(
    prefix="/products",
    tags=["product"]
)


@router.get("/{product_id}")
async def get_product(product_id: int, session: AsyncSession = Depends(get_async_session)):
    try:
        stmt = (
            select(
                product_item.c.id,
                product_category.c.category_name.label("category_name"),
                product_item.c.name,
                product_item.c.description,
                product_item.c.qty_in_stock,
                product_item.c.product_image,
                product_item.c.price,
            )
            .select_from(
                product_item.join(product_category, product_item.c.category_id == product_category.c.id)
            )
            .where(product_item.c.id == product_id)
        )
        result = await session.execute(stmt)
        product_dict = get_product_dict(result)
        if product_dict:
            return {
                "status": "success",
                "data": product_dict,
                "details": None
            }
        else:
            raise HTTPException(status_code=404, detail={
                "status": "error",
                "data": None,
                "details": "Product not found"
            })
    except Exception as e:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": str(e)
        })


@router.get("/")
async def get_all_products(session: AsyncSession = Depends(get_async_session)):
    stmt = (
        select(
            product_item.c.id,
            product_category.c.category_name.label("category_name"),
            product_item.c.name,
            product_item.c.description,
            product_item.c.qty_in_stock,
            product_item.c.product_image,
            product_item.c.price,
        )
        .select_from(
            product_item.join(product_category, product_item.c.category_id == product_category.c.id)
        )
    )
    try:
        result = await session.execute(stmt)
        product_dict = get_product_dict(result)
        if product_dict:
            return {
                "status": "success",
                "data": product_dict,
                "details": None
            }
    except Exception as e:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": str(e)
        })


@router.post("/create_product")
async def create_product(new_product_item: ProductItemSchema, session: AsyncSession = Depends(get_async_session)):
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
