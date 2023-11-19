from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates


router = APIRouter(
    prefix="/main",
    tags=["main"]
)

templates = Jinja2Templates(directory="src/templates/front")


@router.get("/")
def get_main_page(request: Request):
    return templates.TemplateResponse("/main.html", {"request": request})


@router.get("/cart")
def get_main_page(request: Request):
    return templates.TemplateResponse("/cart.html", {"request": request})

