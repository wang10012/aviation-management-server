from dao.seat_table import Seat
from dao.flight_table import Flight


def check_is_seated(seat_code, flight_id):
    flight = Flight.query.filter_by(id=flight_id).first()
    plane_id = flight.plane_id
    seat = Seat.query.filter_by(seat_code=seat_code,
                                plane_id=plane_id).first()
    if seat():
        return True
    else:
        return False
