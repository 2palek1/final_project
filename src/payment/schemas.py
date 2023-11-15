import datetime

from pydantic import BaseModel, BaseConfig


class UserSchema(BaseModel):
    id: int


class PaymentTypeSchema(BaseModel):
    id: int
    value: str


class UserPaymentMethodSchema(BaseModel):
    user_id: int
    payment_type_id: int
    provider: str
    expire_date: datetime = datetime.datetime.utcnow() + datetime.timedelta(hours=6)
    account_number: str
    is_default: bool

    class Config(BaseConfig):
        arbitrary_types_allowed = True
