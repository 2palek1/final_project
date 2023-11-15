from http.client import HTTPException

from sqlalchemy import ResultProxy
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.payment.models import user_payment_method

def get_order_dic(result: ResultProxy):
    order_dict = []
    for row in result.all():
        data = {
            "id": row[0],
            "user_id": row[1],
            "payment_type_id": row[2],
            "provider": row[3],
            "account_number": row[4],
            "expire_date": row[5],
            "is_default": row[7]
        }
        order_dict.append(data)

    return order_dict

async def check_payment_method(user_id: int, session: AsyncSession):
    stmt = select(user_payment_method).where(user_payment_method.user_id == user_id)
    result = await session.execute(stmt)
    payment_methods = result.all()

    if not payment_methods:
        raise HTTPException(status_code=400, detail="User has no valid payment method.")