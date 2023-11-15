from datetime import datetime

from pydantic import BaseModel

class UserSchema(BaseModel):
    id: int

class PaymentTypeSchema(BaseModel):
    id: int
    value: str

class UserPaymentMethodSchema(BaseModel):
    user_id: int
    payment_type_id: int
    provider: str
    account_number: str
    expire_date: datetime.datetime
    is_default: bool
