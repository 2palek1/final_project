from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

# Import product-related functions from the products router
from src.products.router import get_all_products, get_product


# Create an APIRouter instance for the admin section
router = APIRouter(
    prefix="/admin",
    tags=["admin"]
)

# Initialize Jinja2 templates with the specified directory
templates = Jinja2Templates(directory="src/templates/admin")


# Define a route to get the base page
@router.get("/base")
def get_base_page(request: Request):
    return templates.TemplateResponse("/base.html", {"request": request})


# Define a route to get the login page
@router.get("/login")
def get_login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


# Define a route to get the admin dashboard page
@router.get("/dashboard")
def get_admin_page(request: Request):
    return templates.TemplateResponse("/admin.html", {"request": request})


# Define a route to get the users page
@router.get("/users")
def get_users_page(request: Request):
    return templates.TemplateResponse("/users.html", {"request": request})


# Define a route to get the products page with a list of all products
@router.get("/products")
def get_products_page(request: Request, products=Depends(get_all_products)):
    return templates.TemplateResponse("/products.html", {"request": request, "products": products["data"]})


# Define a route to get the products page with details for a specific product
@router.get("/products/{product_id}")
def get_search_page(request: Request, products=Depends(get_product)):
    return templates.TemplateResponse("/products.html", {"request": request, "products": products["data"]})
