from sqlalchemy import ResultProxy


def all_to_dict(result: ResultProxy):
    product_dict = []
    for row in result.all():
        data = {
            "id": row[0],
            "product_id": row[1],
            "SKU": row[2],
            "qty_in_stock": row[3],
            "product_image": row[4],
            "price": row[5]
        }
        product_dict.append(data)
    return product_dict