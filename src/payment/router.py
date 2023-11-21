from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.payment.models import user_payment_method

from src.payment.schemas import UserPaymentMethodSchema
from src.payment.utils import get_payment_dict, check_payment_method


# Create an APIRouter instance for payment-related operations
router = APIRouter(
    prefix='/payment',
    tags=['payment']
)


# Define a route to get payment methods for a user
@router.get("/")
async def get_payment_methods(user_id: int, session: AsyncSession = Depends(get_async_session)):
    try:
        # Check if the user has payment methods, create if not
        await check_payment_method(user_id, session)

        # Retrieve payment methods for the user
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
        # Handle exceptions and return an HTTP error response
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": str(e)
        })


# Define a route to add a new payment method for a user
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
        # Handle exceptions and return an HTTP error response
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": str(e)
        })
