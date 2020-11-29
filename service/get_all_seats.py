from dao.seat_table import Seat
from dao.flight_table import Flight
from dao.plane_table import Plane
from typing import *


def get_all_seats(flight_id):
    flight = Flight.query.filter_by(id=flight_id).first()
    plane = Plane.query.filter_by(id=flight.plane_id).first()
    seats = Seat.query.filter_by(plane_id=plane.id).all()
    result: List[Dict[str]] = [{
        "seat_code": seat.seat_code
    } for seat in seats]
    return result
