from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.order.utilis import get_order_dict
from src.order.models import shop_order
from src.order.schemas import shop_order_schema
from src.database import get_async_session
from sqlalchemy import insert


# Create an APIRouter instance
router = APIRouter()


# Define a route to create a new order
@router.post("/create_order", response_model=shop_order_schema)
async def create_order(order_data: shop_order_schema, session: AsyncSession = Depends(get_async_session)):
    try:
        # Insert the order data into the shop_order table
        stmt = insert(shop_order).values(**order_data.dict())
        await session.execute(stmt)
        await session.commit()

        return {
            "status": "success",
            "data": order_data,
            "details": None
        }
    except Exception as e:
        # Handle exceptions and return an HTTP error response
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": str(e)
        })


# Define a route to read details of a specific order by ID
@router.get("/order/{order_id}", response_model=shop_order_schema)
async def read_order(order_id: int, session: AsyncSession = Depends(get_async_session)):
    # Select the order data from the shop_order table based on order ID
    stmt = shop_order.select().where(shop_order.c.id == order_id)
    result = await session.execute(stmt)
    order_data = result.fetchone()

    if not order_data:
        # If the order is not found, raise a 404 HTTPException
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )
    return order_data


# Define a route to get a list of all orders
@router.get("/order_list", response_model=list[shop_order_schema])
async def get_order_list(session: AsyncSession = Depends(get_async_session)):
    # Select all orders from the shop_order table
    stmt = shop_order.select()
    result = await session.execute(stmt)
    order_list = get_order_dict(result)

    return order_list
