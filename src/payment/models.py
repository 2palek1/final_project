from datetime import datetime

from sqlalchemy import Table, Column, Integer, String, ForeignKey, MetaData, TIMESTAMP, Boolean

from src.auth.models import user

metadata = MetaData()


payment_type = Table(
    "payment_type",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("value", String, nullable=False)
)

user_payment_method = Table(
    "user_payment_method",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey(user.c.id)),
    Column("payment_type_id", Integer, ForeignKey(payment_type.c.id)),
    Column("provider", String, nullable=False),
    Column("account_number", String, nullable=False),
    Column("expire_date", TIMESTAMP, default=datetime.utcnow()),
    Column("is_default", Boolean, nullable=False)
)

