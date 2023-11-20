from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from src.products.router import get_all_products

router = APIRouter(
    prefix="/main",
    tags=["main"]
)

templates = Jinja2Templates(directory="src/templates/front")


@router.get("/")
def get_main_page(request: Request, products=Depends(get_all_products)):
    return templates.TemplateResponse("/main.html", {"request": request, "products": products["data"]})


@router.get("/cart")
def get_main_page(request: Request):
    return templates.TemplateResponse("/cart.html", {"request": request})
