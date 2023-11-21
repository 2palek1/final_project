from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

# Import product-related functions from the products router
from src.products.router import get_all_products, get_products_by_category


# Create an APIRouter instance for the main section
router = APIRouter(
    prefix="/main",
    tags=["main"]
)

# Initialize Jinja2 templates with the specified directory
templates = Jinja2Templates(directory="src/templates/front")


# Define a route to get the main page with a list of all products
@router.get("/")
def get_main_page(request: Request, products=Depends(get_all_products)):
    return templates.TemplateResponse("/main.html", {"request": request, "products": products["data"]})


# Define a route to get the cart page
@router.get("/cart")
def get_cart_page(request: Request):
    return templates.TemplateResponse("/cart.html", {"request": request})


# Define a route to get the catalog page
@router.get("/catalog")
def get_catalog_page(request: Request):
    return templates.TemplateResponse("/catalog.html", {"request": request})


# Define a route to get the category page with a list of products for a specific category
@router.get("/category")
def get_catalog_page(request: Request, products=Depends(get_products_by_category)):
    return templates.TemplateResponse("/category.html", {"request": request, "products": products["data"]})


# Define a route to get the services page
@router.get("/services")
def get_services_page(request: Request):
    return templates.TemplateResponse("/services.html", {"request": request})


# Define a route to get the about page
@router.get("/about")
def get_about_page(request: Request):
    return templates.TemplateResponse("/about.html", {"request": request})


# Define a route to get the products page with a list of all products
@router.get("/products")
def get_products_page(request: Request, products=Depends(get_all_products)):
    return templates.TemplateResponse("/products.html", {"request": request, "products": products["data"]})
