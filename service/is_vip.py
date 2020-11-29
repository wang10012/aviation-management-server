from dao.vip_customer_table import VIPCustomer


def is_vip(customer_username):
    vipcustomer = VIPCustomer.query.filter_by(username=customer_username).first()
    if vipcustomer:
        return True
    else:
        return False
