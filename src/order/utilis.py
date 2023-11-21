from sqlalchemy import ResultProxy


# Utility function to convert a ResultProxy of order data to a list of dictionaries
def get_order_dict(result: ResultProxy):
    order_dict = []
    for row in result.all():
        # Extract order details from the ResultProxy row and create a dictionary
        data = {
            "id": row[0],
            "user_id": row[1],
            "order_date": row[2],
            "payment_method_id": row[3],
            "shipping_address": row[4],
            "shipping_method": row[5],
            "order_total": row[6],
            "order_status": row[7]
        }
        # Add the dictionary to the list
        order_dict.append(data)

    return order_dict
