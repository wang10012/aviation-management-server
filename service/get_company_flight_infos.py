from dao.flight_table import Flight
from typing import *


def get_company_flight_infos(company_name):
    company_flight_infos = Flight.query.filter_by(air_company_name=company_name).all()
    results: List[Dict[str]] = [
        {
            'flight_id': company_flight_info.id,
            'start_time': str(company_flight_info.start_time),
            'arrive_time': str(company_flight_info.arrive_time),
            'first_class_price': company_flight_info.first_class_price,
            'business_class_price': company_flight_info.business_class_price,
            'economy_class_price': company_flight_info.economy_class_price,
            'num_remain_seat': company_flight_info.num_remain_seat,
            'num_remain_first_class': company_flight_info.num_remain_first_class,
            'num_remain_business_class': company_flight_info.num_remain_business_class,
            'num_remain_economy_class': company_flight_info.num_remain_economy_class,
            'airport_id': company_flight_info.airport_id,
            'plane_id': company_flight_info.plane_id,
            'company_name': company_flight_info.air_company_name,
            'airline_id': company_flight_info.air_line_id,
        } for company_flight_info in company_flight_infos
    ]
    return results
