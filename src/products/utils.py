from sqlalchemy import ResultProxy


# Utility function to convert a ResultProxy of product data to a list of dictionaries
def get_product_dict(result: ResultProxy):
    product_dict = []
    for row in result.all():
        # Extract product details from the ResultProxy row and create a dictionary
        data = {
            "id": row[0],
            "category": row[1],
            "name": row[2],
            "description": row[3],
            "qty_in_stock": row[4],
            "product_image": row[5],
            "price": row[6]
        }
        # Add the dictionary to the list
        product_dict.append(data)
    return product_dict
