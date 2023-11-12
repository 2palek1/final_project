from pydantic import BaseModel


class ShoppingCart(BaseModel):
    user_id: int


class ShoppingCartItem(BaseModel):
    cart_id: int
    product_item_id: int
    qty: int
