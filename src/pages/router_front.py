from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from src.products.router import get_all_products, get_products_by_category

router = APIRouter(
    prefix="/main",
    tags=["main"]
)

templates = Jinja2Templates(directory="src/templates/front")


@router.get("/")
def get_main_page(request: Request, products=Depends(get_all_products)):
    return templates.TemplateResponse("/main.html", {"request": request, "products": products["data"]})


@router.get("/cart")
def get_cart_page(request: Request):
    return templates.TemplateResponse("/cart.html", {"request": request})


@router.get("/catalog")
def get_catalog_page(request: Request):
    return templates.TemplateResponse("/catalog.html", {"request": request})


@router.get("/category")
def get_catalog_page(request: Request, products=Depends(get_products_by_category)):
    return templates.TemplateResponse("/category.html", {"request": request, "products": products["data"]})


@router.get("/services")
def get_services_page(request: Request):
    return templates.TemplateResponse("/services.html", {"request": request})

@router.get("/about")
def get_about_page(request: Request):
    return templates.TemplateResponse("/about.html", {"request": request})

