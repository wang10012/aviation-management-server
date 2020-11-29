from dao.air_company_table import AirCompany
from typing import *


def get_company_info(name):
    company = AirCompany.query.filter_by(name=name).first()
    result: Dict[str] = {
        'company_name': company.name,
        'company_password': company.password,
        'call_number': company.call_number,
    }
    return result
