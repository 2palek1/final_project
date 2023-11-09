from pydantic import BaseModel


class ProductSchema(BaseModel):
    name: str
    quantity: str
    description: str
    product_image: str

