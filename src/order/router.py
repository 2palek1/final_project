from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.order.utilis import get_order_dict
from src.order.models import shop_order, order_status, shipping_method
from src.order.schemas import shop_order_schema, order_status_schema, shipping_method_schema
from src.database import get_async_session
from sqlalchemy import select, insert, delete

router = APIRouter()

@router.post("/create_order", response_model=shop_order_schema)
async def create_order(order_data: shop_order_schema, session: AsyncSession = Depends(get_async_session)):
    try:
        stmt = insert(shop_order).values(**order_data.dict())
        await session.execute(stmt)
        await session.commit()
        return {
            "status": "success",
            "data": order_data,
            "details": None
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": str(e)
        })

@router.get("/order/{order_id}", response_model=shop_order_schema)
async def read_order(order_id: int, session: AsyncSession = Depends(get_async_session)):
    stmt = shop_order.select().where(shop_order.c.id == order_id)
    result = await session.execute(stmt)
    order_data = result.fetchone()

    if not order_data:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )
    return order_data

@router.get("/order_list", response_model=list[shop_order_schema])
async def get_order_list(session: AsyncSession = Depends(get_async_session())):
    stmt = shop_order.select()
    result = await session.execute(stmt)
    order_list = get_order_dict(result)

    return order_list