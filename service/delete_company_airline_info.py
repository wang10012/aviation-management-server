from dao.aircompany_airline_table import AircompanyAirline
from global_var import db


def delete_company_airline_info(company_airline_id):
    company_airline = AircompanyAirline.query.filter_by(id=company_airline_id).first()
    if company_airline:
        db.session.delete(company_airline)
    else:
        return False
    db.session.commit()
    return True

