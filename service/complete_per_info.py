from dao.customer_table import Customer
from global_var import db


def complete_per_info(username, age, gender, ID_number):
    customer = Customer.query.filter_by(username=username).first()
    if customer:
        customer.age = age
        customer.gender = gender
        customer.ID_number = ID_number
    else:
        return False  # 没有必要了，一定找的到
    db.session.commit()
    return True
