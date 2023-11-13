from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.cart.models import shopping_cart, shopping_cart_item
from src.cart.schemas import ShoppingCartItem


router = APIRouter(
    prefix="/cart",
    tags=["cart"]
)


async def check_cart(user_id: int, session: AsyncSession = Depends(get_async_session)):
    existing_cart = await session.execute(select(shopping_cart).where(shopping_cart.c.user_id == user_id))
    cart = existing_cart.scalar_one_or_none()
    if cart is None:
        # If the cart doesn't exist, create a new one
        cart_data = {"user_id": user_id}
        stmt = insert(shopping_cart).values(cart_data)
        await session.execute(stmt)
        await session.commit()
        return f"user_id: {user_id} - cart created"
    return f"user_id: {user_id} - cart already exists"


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
        cart_data = result.scalar()
        return {
            "status": "success",
            "data": cart_data,
            "details": None
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": str(e)
        })
