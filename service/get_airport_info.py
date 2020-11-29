from dao.airport_table import Airport
from typing import *


def get_airport_info():
    airport_infos = Airport.query.all()
    results: List[Dict[str]] = [
        {
            'airport_id': airport_info.id,
            'start_name': airport_info.start_name,
            'arrive_name': airport_info.arrive_name,
        } for airport_info in airport_infos
    ]
    return results
