from dao.aircompany_airline_table import AircompanyAirline
from global_var import db


def add_company_airline_info(company_name, airline_id):
    company_airline = AircompanyAirline.query.filter_by(air_company_name=company_name,
                                                        air_line_id=airline_id).first()
    if not company_airline:
        company_airline = AircompanyAirline(
            air_company_name=company_name,
            air_line_id=airline_id
        )
        db.session.add(company_airline)
    else:
        return False
    db.session.commit()
    return True
