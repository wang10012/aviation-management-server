from dao.aircompany_airline_table import AircompanyAirline
from typing import *


def get_company_airline_info(company_name):
    company_airline_infos = AircompanyAirline.query.filter_by(air_company_name=company_name).all()
    results: List[Dict[str]] = [
        {
            'company_airline_id': company_airline_info.id,
            'company_name': company_airline_info.air_company_name,
            'airline_id': company_airline_info.air_line_id,
        } for company_airline_info in company_airline_infos
    ]
    return results
