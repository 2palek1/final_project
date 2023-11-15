from fastapi import HTTPException

from sqlalchemy import ResultProxy
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.payment.models import user_payment_method


def get_payment_dict(result: ResultProxy):
    order_dict = []
    for row in result.all():
        data = {
            "id": row[0],
            "user_id": row[1],
            "payment_type_id": row[2],
            "provider": row[3],
            "account_number": row[4],
            "expire_date": row[5],
            "is_default": row[6]
        }
        order_dict.append(data)

    return order_dict


async def check_payment_method(user_id: int, session: AsyncSession):
    stmt = select(user_payment_method).where(user_payment_method.c.user_id == user_id)
    result = await session.execute(stmt)
    payment_methods = result.all()

    if not payment_methods:
        raise HTTPException(status_code=400, detail={
            "status": "error",
            "data": None,
            "details": "User does not have any payment method"
        })