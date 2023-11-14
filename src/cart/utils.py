from fastapi import Depends
from sqlalchemy import ResultProxy, select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.cart.models import shopping_cart
from src.database import get_async_session


def get_cart_dict(result: ResultProxy):
    cart_dict = []
    for row in result.all():
        data = {
            "id": row[0],
            "cart_id": row[1],
            "product_item_id": row[2],
            "qty": row[3]
        }
        cart_dict.append(data)
    return cart_dict


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
