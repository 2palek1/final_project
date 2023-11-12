from pydantic import BaseModel


class shopping_cart_SCHEMA(BaseModel):
    user_id: int

class shopping_cart_item_SCHEMA(BaseModel):
    cart_id: int
    product_item_id: int
    qty: int
