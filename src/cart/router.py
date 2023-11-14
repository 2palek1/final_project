from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.cart.utils import get_cart_dict, check_cart
from src.database import get_async_session
from src.cart.models import shopping_cart, shopping_cart_item
from src.cart.schemas import ShoppingCartItem


router = APIRouter(
    prefix="/cart",
    tags=["cart"]
)


@router.post("/add")
async def add_item(user_id: int, item: ShoppingCartItem, session: AsyncSession = Depends(get_async_session)):
    try:
        await check_cart(user_id, session)

        # Add the shopping cart item to the cart
        stmt = insert(shopping_cart_item).values(**item.dict())
        result = await session.execute(stmt)
        await session.commit()

        return {
            "status": "success",
            "data": result.all(),
            "details": None
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": str(e)
        })


@router.get("/{user_id}")
async def get_cart(user_id: int, session: AsyncSession = Depends(get_async_session)):
    try:
        # Check if the shopping cart exists for the user
        await check_cart(user_id, session)

        stmt = select(shopping_cart.c.id).where(shopping_cart.c.user_id == user_id)
        result = await session.execute(stmt)
        cart_id = result.scalar_one()

        stmt = select(shopping_cart_item).where(shopping_cart_item.c.cart_id == cart_id)
        result = await session.execute(stmt)
        cart_data_dict = get_cart_dict(result)
        return {
            "status": "success",
            "data": cart_data_dict,
            "details": None
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": str(e)
        })
