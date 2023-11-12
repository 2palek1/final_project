from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.cart.models import shopping_cart, shopping_cart_item
from src.cart.schemas import shopping_cart_SCHEMA, shopping_cart_item_SCHEMA


router = APIRouter(
    prefix="/cart",
    tags=["cart"]
)


@router.post("/create_cart")
async def create_cart(new_cart: shopping_cart_item_SCHEMA, session: AsyncSession=Depends(get_async_session)):
    try:
        stmt = insert(shopping_cart).values(**new_cart.dict())
        result =await session.execute(stmt)
        await session.commit()
        return {"status":"Запрос принят", "data":result.rowcount, "details":None}
    except Exception as e:
        raise HTTPException(status_code=500, detail={"status":"error", "data":None,"details":str(e)})


@router.post("/add_to_cart")
async def at_to_cart(item: shopping_cart_item_SCHEMA, session: AsyncSession = Depends(get_async_session)):
    try:
        stmt = insert(shopping_cart_item).values(**item.dict())
        result = await session.expire(stmt)
        await session.commit()
        return {"status":"Запрос принят", "data":result.rowcount,"details":None}
    except Exception as e:
        raise HTTPException(status_code=500, detail={"status":"error", "data":None,"details":str(e)})

@router.get("/get_cart/{user_id}")
async def get_cart(user_id:int, session: AsyncSession = Depends(get_async_session)):
    try:
        stmt = select(shopping_cart).where(shopping_cart.c.user_id == user_id)
        result = await session.execute(stmt)
        cart_data = result.scalar_one()
        return {"status":"Запрос принят", "data":cart_data,"details":None}
    except Exception as e:
        raise HTTPException(status_code=500, detail={"status":"error", "data":None, "details": str(e)})