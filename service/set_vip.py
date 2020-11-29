from dao.customer_table import Customer
from dao.vip_customer_table import VIPCustomer
from global_var import db


def set_vip(username):
    vip_customer = VIPCustomer.query.filter_by(username=username).first()
    customer = Customer.query.filter_by(username=username).first()
    if not vip_customer:
        customer.type = 'VIP'
        vip_customer = VIPCustomer(
            username=username
        )
        db.session.add(vip_customer)
    else:
        return False
    db.session.commit()
    return True
