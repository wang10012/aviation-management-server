from dao.air_company_table import AirCompany
from dao.aircompany_airline_table import AircompanyAirline
from dao.aircompany_plane_table import AircompanyPlane
from dao.airline_table import AirLine
from dao.airport_table import Airport
from dao.flight_table import Flight
from dao.plane_table import Plane
from typing import *

from global_var import db


def get_flight(start, destination, airline_date):
    #     注意可能session中断对其有影响，最好在service层就取出来放进一个列表里
    flights = db.session.query(
        AirCompany.name,
        Flight.id,
        Flight.start_time,
        Flight.arrive_time,
        Plane.id,
        Airport.start_name,
        Airport.arrive_name,
        Flight.economy_class_price,
        Flight.business_class_price,
        Flight.first_class_price,
        # add
        Flight.num_remain_seat,
        Flight.num_remain_first_class,
        Flight.num_remain_business_class,
        Flight.num_remain_economy_class

    ).filter(
        AirLine.start == start,
        AirLine.destination == destination,
        AirLine.airline_date == airline_date,
        Flight.air_line_id == AirLine.id,
        Flight.airport_id == Airport.id,
        Flight.plane_id == Plane.id,
        Flight.air_company_name == AirCompany.name,
        AirLine.id == AircompanyAirline.air_line_id,
        AircompanyAirline.air_company_name == AirCompany.name,
        Plane.id == AircompanyPlane.plane_id
    ).distinct().all()
    results: List[Dict[str]] = [{
        'air_company_name': air_company_name,
        'flight_id': flight_id,
        'start_time': str(start_time),
        'arrive_time': str(arrive_time),
        'plane_id': plane_id,
        'start_airport_name': start_airport_name,
        'arrive_airport_name': arrive_airport_name,
        'lowest_price': lowest_price,
        'business_class_price': business_class_price,
        'first_class_price': first_class_price,
        # add
        'num_remain_seat': num_remain_seat,
        'num_remain_first_class': num_remain_first_class,
        'num_remain_business_class': num_remain_business_class,
        'num_remain_economy_class': num_remain_economy_class
    } for
        air_company_name,
        flight_id,
        start_time,
        arrive_time,
        plane_id,
        start_airport_name,
        arrive_airport_name,
        lowest_price,
        business_class_price,
        first_class_price,


        num_remain_seat,
        num_remain_first_class,
        num_remain_business_class,
        num_remain_economy_class
        in flights]

    return results
