from datetime import datetime, timedelta

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.payment.models import user_payment_method

from src.payment.schemas import UserPaymentMethodSchema
from src.payment.utils import get_payment_dict, check_payment_method


router = APIRouter(
    prefix='/payment',
    tags=['payment']
)


@router.get("/")
async def get_payment_methods(user_id: int, session: AsyncSession = Depends(get_async_session)):
    try:
        await check_payment_method(user_id, session)

        stmt = select(user_payment_method).where(user_payment_method.c.user_id == user_id)
        result = await session.execute(stmt)
        payment_methods = get_payment_dict(result)

        if payment_methods:
            return {
                "status": "success",
                "data": payment_methods,
                "details": None
            }
    except Exception as e:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": str(e)
        })


@router.post("/add")
async def add_payment_method(payment_method: UserPaymentMethodSchema, session: AsyncSession = Depends(get_async_session)):
    try:
        # Add the new payment method
        stmt = insert(user_payment_method).values(**payment_method.dict())
        result = await session.execute(stmt)
        await session.commit()
        return {
            "status": "success",
            "data": get_payment_dict(result),
            "details": "Payment method added successfully."
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": str(e)
        })


# @router.get("/get_payment_types", response_model=list[PaymentTypeSchema])
# async def get_payment_types(session: AsyncSession = Depends(get_async_session)):
#     stmt = select(payment_type)
#     result = await session.execute(stmt)
#     payment_types = result.all()
#
#     return {
#         "status": "success",
#         "data": payment_types,
#         "details": None
#     }
