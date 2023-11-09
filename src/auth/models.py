from datetime import datetime

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, JSON, MetaData, ForeignKey, Boolean

from src.database import Base

metadata = MetaData()

role = Table(
    "role",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("permissions", JSON)
)

user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, nullable=False),
    Column("phone_number", String, nullable=False),
    Column("username", String, nullable=False),
    Column("hashed_password", String, nullable=False),
    Column("registered_at", TIMESTAMP, default=datetime.utcnow()),
    Column("role_id", Integer, ForeignKey(role.c.id)),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False)
)

address = Table(
    "address",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("unit_number", String),
    Column("street_number", String, nullable=False),
    Column("address_line1", String, nullable=False),
    Column("address_line2", String, nullable=False),
    Column("city", String, nullable=False),
    Column("region", String, nullable=False),
    Column("postal_code", String, nullable=False)
)

user_address = Table(
    "user_address",
    metadata,
    Column("user_id", Integer, ForeignKey(user.c.id)),
    Column("address_id", Integer, ForeignKey(address.c.id))
)


class User(SQLAlchemyBaseUserTable[int], Base):
    id = Column("id", Integer, primary_key=True)
    email = Column("email", String, nullable=False)
    username = Column("username", String, nullable=False)
    phone_number = Column("phone_number", String, nullable=False)
    registered_at = Column("registered_at", TIMESTAMP, default=datetime.utcnow())
    role_id = Column("role_id", Integer, ForeignKey(role.c.id))
    hashed_password: str = Column(String(length=1024), nullable=False)
    is_active: bool = Column(Boolean, default=True, nullable=False)
    is_superuser: bool = Column(Boolean, default=False, nullable=False)
    is_verified: bool = Column(Boolean, default=False, nullable=False)
