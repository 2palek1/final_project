from fastapi import FastAPI, Depends

from src.auth.base_config import fastapi_users, auth_backend
from src.products.router import router as router_products
from src.cart.router import router as router_cart
from src.auth.schemas import UserRead, UserCreate


app = FastAPI(
    title="Final Project"
)


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
