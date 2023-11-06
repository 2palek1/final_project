from pydantic import BaseModel
from typing import List

class CardSchema(BaseModel):
    address_line: str
    address_city: str
    address_country: str
    address_zip: str

class TokenSchema(BaseModel):
    id: str
    email: str
    card: CardSchema

class CartItemSchema(BaseModel):
    name: str
    quantity: id
    price: int

class CurrentUserSchema(BaseModel):
    id: int
    name: str
    email: str
    is_staff: bool
    is_active: bool

class OrderCreatePlaceOrder(BaseModel):
    token: TokenSchema
    cartItems: List[CartItemSchema]
    currentUser: CurrentUserSchema
    subtotal: int