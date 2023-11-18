from fastapi import FastAPI, Depends
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi.staticfiles import StaticFiles

from src.auth.base_config import fastapi_users, auth_backend
from src.products.router import router as router_products
from src.cart.router import router as router_cart
from src.payment.router import router as router_payment
from src.auth.schemas import UserRead, UserCreate
from src.pages.router import router as router_pages

from redis import asyncio as aioredis

app = FastAPI(
    title="Final Project"
)


# Mount the "styles" directory as a static directory
app.mount("/pages/styles", StaticFiles(directory=str("src/templates/styles")), name="styles")


app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)


app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)


app.include_router(router_products)
app.include_router(router_cart)
app.include_router(router_pages)
app.include_router(router_payment)


@app.on_event("startup")
async def startup_event():
    redis = aioredis.from_url("redis://localhost", encoding="UTF-8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
