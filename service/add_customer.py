from dao.customer_table import Customer
from global_var import db


# 注册时添加
def add_customer(name, username, password, phone_number):
    customer = Customer.query.filter_by(username=username).first()
    if not customer:
        customer = Customer(
            name=name,
            username=username,
            password=password,
            phone_number=phone_number
        )
        db.session.add(customer)
    else:
        return False
    db.session.commit()
    return True
