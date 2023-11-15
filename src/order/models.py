from datetime import datetime

from sqlalchemy import Table, Column, Integer, String, ForeignKey, MetaData, TIMESTAMP

from src.auth.models import user, address
from src.payment.models import user_payment_method

metadata = MetaData()

shipping_method = Table(
    "shipping_method",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("price", Integer, nullable=False)
)

order_status = Table(
    "order_status",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("status", String, nullable=False)
)

shop_order = Table(
    "shop_order",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey(user.c.id)),
    Column("order_date", TIMESTAMP, default=datetime.utcnow()),
    Column("payment_method_id", Integer, ForeignKey(user_payment_method.c.id)),
    Column("shipping_address", Integer, ForeignKey(address.c.id)),
    Column("shipping_method", Integer, ForeignKey(shipping_method.c.id)),
    Column("order_total", Integer, nullable=False),
    Column("order_status", Integer, ForeignKey(order_status.c.id))
)