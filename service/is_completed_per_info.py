from dao.customer_table import Customer


def is_completed_per_info(username):
    customer = Customer.query.filter_by(username=username).first()
    if customer.age is None or customer.gender is None or customer.ID_number is None:
        return False
    else:
        return True
