from dao.customer_table import Customer
from typing import *


def get_customer_info(username):
    customer = Customer.query.filter_by(username=username).first()
    result: Dict[str] = {
        'username': customer.username,
        'name': customer.name,
        'password': customer.password,
        'phone_number': customer.phone_number,
        'age': customer.age,
        'gender': customer.gender,
        'ID_number': customer.ID_number
    }
    return result
