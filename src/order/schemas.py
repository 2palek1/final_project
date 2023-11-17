from pydantic import BaseModel, BaseConfig
import datetime


class shop_order_schema(BaseModel):
    user_id: int
    order_date: datetime.datetime.utcnow() + datetime.timedelta(hours=6)
    payment_method_id: int
    shipping_address: int
    shipping_method: int
    order_total: int
    order_status: int

class order_status_schema(BaseModel):
    id: int
    status: str

class shipping_method_schema(BaseModel):
    id: int
    name: str
    price: int

