from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates


router = APIRouter(
    prefix="/",
    tags=["Pages"]
)

templates = Jinja2Templates(directory="src/templates/front")