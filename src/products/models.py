from sqlalchemy import Integer, String, Table, Column, ForeignKey, MetaData


metadata = MetaData()


product_category = Table(
    "product_category",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("category_name", String, nullable=False),
)

product = Table(
    "product",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("category_id", Integer, ForeignKey(product_category.c.id)),
    Column("name", String, nullable=False),
    Column("description", String, nullable=False),
    Column("product_image", String, nullable=False)
)

product_item = Table(
    "product_item",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("product_id", Integer, ForeignKey(product.c.id)),
    Column("SKU", Integer, nullable=False),
    Column("qty_in_stock", Integer, nullable=False),
    Column("product_image", String, nullable=False),
    Column("price", Integer, nullable=False),
)


variation = Table(
    "variation",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("category_id", Integer, ForeignKey(product_category.c.id)),
    Column("name", String, nullable=False)
)

variation_option = Table(
    "variation_option",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("variation_id", Integer, ForeignKey(variation.c.id)),
    Column("value", String, nullable=False)
)

product_configuration = Table(
    "product_configuration",
    metadata,
    Column("product_item_id", Integer, ForeignKey(product_item.c.id)),
    Column("variation_option_id", Integer, ForeignKey(variation_option.c.id))
)

