from pydantic import BaseModel
from typing import List

class ProductScheme(BaseModel):
    name: str
    image: str
    category: str
    description: str
    price: int
    countInStock: int