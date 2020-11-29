from dao.air_company_table import AirCompany
from global_var import db


def complete_company_info(company_name, company_password, call_number):
    company = AirCompany.query.filter_by(name=company_name).first()
    if company:
        company.password = company_password
        company.call_number = call_number
    else:
        return False  # 没有必要了，一定找的到
    db.session.commit()
    return True
