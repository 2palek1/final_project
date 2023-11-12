from sqlalchemy import Table, Column, Integer, ForeignKey, MetaData

from src.auth.models import user
from src.products.models import product_item

metadata = MetaData()

shopping_cart = Table(
    "shopping_cart",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey(user.c.id))
)

shopping_cart_item = Table(
    "shopping_cart_item",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("cart_id", Integer, ForeignKey(shopping_cart.c.id)),
    Column("product_item_id", Integer, ForeignKey(product_item.c.id)),
    Column("qty", Integer, nullable=False)
)
