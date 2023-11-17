from pydantic import BaseModel


class ProductItemSchema(BaseModel):
    category_id: int
    name: str
    description: str
    qty_in_stock: int
    product_image: str
    price: int

