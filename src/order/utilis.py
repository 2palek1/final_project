from sqlalchemy import ResultProxy


def get_order_dict(result: ResultProxy):
    order_dict = []
    for row in result.all():
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
        order_dict.append(data)

    return order_dict
