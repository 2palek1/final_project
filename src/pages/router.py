from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates


from src.products.router import get_all_products, get_product

router = APIRouter(
    prefix="/pages",
    tags=["Pages"]
)

templates = Jinja2Templates(directory="src/templates/admin")


@router.get("/base")
def get_base_page(request: Request):
    return templates.TemplateResponse("/base.html", {"request": request})


@router.get("/login")
def get_login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@router.get("/admin")
def get_admin_page(request: Request):
    return templates.TemplateResponse("/admin.html", {"request": request})


@router.get("/users")
def get_users_page(request: Request):
    return templates.TemplateResponse("/users.html", {"request": request})


@router.get("/products")
def get_products_page(request: Request, products=Depends(get_all_products)):
    return templates.TemplateResponse("/products.html", {"request": request, "products": products["data"]})


@router.get("/products/{product_id}")
def get_search_page(request: Request, products=Depends(get_product)):
    return templates.TemplateResponse("/products.html", {"request": request, "products": products["data"]})
