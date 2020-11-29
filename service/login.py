from dao.customer_table import Customer
from dao.air_company_table import AirCompany


def customer_login(username, password):
    return bool(Customer.query.filter_by(username=username, password=password).first())


def admin_login(name, password):
    return bool(AirCompany.query.filter_by(name=name, password=password).first())
