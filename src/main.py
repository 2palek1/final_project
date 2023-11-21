from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from src.auth.base_config import fastapi_users, auth_backend
from src.products.router import router as router_products
from src.cart.router import router as router_cart
from src.payment.router import router as router_payment
from src.auth.schemas import UserRead, UserCreate
from src.pages.router_admin import router as router_pages
from src.pages.router_front import router as router_front

from redis import asyncio as aioredis

app = FastAPI(
    title="Final Project"
)


origins = ["http://127.0.0.1:8000", "http://localhost:8000", "http://localhost:3000"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Mount the "styles" directory as a static directory
app.mount("/pages/styles", StaticFiles(directory=str("src/templates/styles")), name="styles")
# Mount the "styles" directory as a static directory
app.mount("/main/styles", StaticFiles(directory=str("src/templates/styles")), name="styles")
app.mount("/main/static", StaticFiles(directory=str("src/static")), name="static")


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

app.include_router(
    fastapi_users.get_users_router(UserRead, UserCreate),
    prefix="/auth/users",
    tags=["auth"],
)


app.include_router(router_products)
app.include_router(router_cart)
app.include_router(router_pages)
app.include_router(router_payment)
app.include_router(router_front)


@app.on_event("startup")
async def startup_event():
    redis = aioredis.from_url("redis://localhost", encoding="UTF-8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
