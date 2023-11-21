from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base

from src.config import DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME


# Define the URL for connecting to the PostgreSQL database using asyncpg
DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Create a SQLAlchemy declarative base for defining models
Base: DeclarativeMeta = declarative_base()

# Create an asynchronous engine for database operations
engine = create_async_engine(DATABASE_URL)

# Create an asynchronous session maker with the specified engine
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


# Define an asynchronous function to get an async session using a generator
async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    # Use a context manager to create and manage an async session
    async with async_session_maker() as session:
        # Yield the async session to the caller
        yield session
