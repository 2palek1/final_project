from pydantic import BaseModel


class ProductSchema(BaseModel):
    category_id: int
    name: str
    description: str
    product_image: str


class ProductItemSchema(BaseModel):
    product_id: int
    SKU: int
    qty_in_stock: int
    product_image: str
    price: int
