from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, insert, delete
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.products.models import product_item, product_category
from src.products.schemas import ProductItemSchema
from src.products.utils import get_product_dict

# Create an APIRouter instance
router = APIRouter(
    prefix="/products",
    tags=["product"]
)


# Define a route to get a single product by ID
@router.get("/{product_id}")
async def get_product(product_id: int, session: AsyncSession = Depends(get_async_session)):
    try:
        # Build a SQL statement to select product details and category name using joins
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


# Define a route to get all products
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


# Define a route to get products by category
@router.get("/category/{category_id}")
async def get_products_by_category(category_id: int, session: AsyncSession = Depends(get_async_session)):
    stmt = select(product_item).where(product_item.c.category_id == category_id)
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


# Define a route to create a new product
@router.post("/create_product")
async def create_product(new_product_item: ProductItemSchema, session: AsyncSession = Depends(get_async_session)):
    try:
        # Build a SQL statement to insert a new product using the provided schema
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


# Define a route to delete a product by ID
@router.delete("/delete/{product_id}")
async def delete_product(product_id: int, session: AsyncSession = Depends(get_async_session)):
    try:
        # Build a SQL statement to delete a product by ID
        stmt = delete(product_item).where(product_item.c.id == product_id)
        await session.execute(stmt)
        await session.commit()
        return {
            "status": "success",
            "data": product_id,
            "details": None
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail={
            "status": "failed",
            "data": None,
            "details": str(e)
        })