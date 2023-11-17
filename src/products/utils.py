from sqlalchemy import ResultProxy


def get_product_dict(result: ResultProxy):
    product_dict = []
    for row in result.all():
        data = {
            "id": row[0],
            "category": row[1],
            "name": row[2],
            "description": row[3],
            "qty_in_stock": row[4],
            "product_image": row[5],
            "price": row[6]
        }
        product_dict.append(data)
    return product_dict
