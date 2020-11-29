from dao.air_company_table import AirCompany
from global_var import db


def add_company(name, password):
    company = AirCompany.query.filter_by(name=name).first()
    if not company:
        company = AirCompany(
            name=name,
            password=password,
        )
        db.session.add(company)
    else:
        return False
    db.session.commit()
    return True