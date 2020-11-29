from dao.ticket_table import Ticket
from dao.flight_table import Flight
from dao.plane_table import Plane
from dao.airport_table import Airport
from dao.seat_table import Seat
from dao.airline_table import AirLine
from typing import *
from global_var import db


def get_ticket(username):
    tickets = db.session.query(
        Ticket.id,
        Ticket.flight_id,
        Ticket.ticket_class,
        Ticket.ticket_pay_price,
        Flight.start_time,
        Flight.arrive_time,
        AirLine.start,
        AirLine.destination,
        AirLine.airline_date,
        Plane.id,
        Airport.start_name,
        Airport.arrive_name,
        Seat.seat_code
    ).filter(
        Ticket.customer_username == username,
        Ticket.flight_id == Flight.id,
        Ticket.seat_id == Seat.id,
        Flight.airport_id == Airport.id,
        Flight.plane_id == Plane.id,
        Flight.air_line_id == AirLine.id,
    ).distinct().all()
    results: List[Dict[str]] = [{
        'ticket_id': ticket_id,
        'flight_id': flight_id,
        'ticket_class': ticket_class,
        'ticket_pay_price': ticket_pay_price,
        'start_time': str(start_time),
        'arrive_time': str(arrive_time),
        'start': start,
        'destination': destination,
        'airline_date': airline_date,
        'plane_id': plane_id,
        'start_airport_name': start_airport_name,
        'arrive_airport_name': arrive_airport_name,
        'seat_code': seat_code
    } for
        ticket_id,
        flight_id,
        ticket_class,
        ticket_pay_price,
        start_time,
        arrive_time,
        start,
        destination,
        airline_date,
        plane_id,
        start_airport_name,
        arrive_airport_name,
        seat_code

        in tickets]

    return results
