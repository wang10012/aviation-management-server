from dao.seat_table import Seat
from dao.plane_table import Plane
from dao.flight_table import Flight
from dao.ticket_table import Ticket
from global_var import db


# def add_seat(seat_code, seat_type, plane_id):
#     seat = Seat.query.filter_by(seat_code=seat_code,
#                                 seat_type=seat_type,
#                                 plane_id=plane_id).first()
#
#     if not seat:
#         seat = Seat(
#             seat_code=seat_code,
#             seat_type=seat_type,
#             plane_id=plane_id
#         )
#         db.session.add(seat)
#     else:
#         return False
#     db.session.commit()
#     return True


def add_seat(customer_username, flight_id, ticket_class, seat_code):
    flight = Flight.query.filter_by(id=flight_id).first()
    plane_id = flight.plane_id
    seat = Seat.query.filter_by(seat_code=seat_code,
                                seat_type=ticket_class,
                                plane_id=plane_id).first()
    ticket = Ticket.query.filter_by(customer_username=customer_username,
                                    flight_id=flight_id,
                                    ticket_class=ticket_class).first()
    if not seat:
        seat = Seat(
            seat_code=seat_code,
            seat_type=ticket_class,
            plane_id=plane_id
        )
        db.session.add(seat)
        seat_ = Seat.query.filter_by(seat_code=seat_code,
                                     seat_type=ticket_class,
                                     plane_id=plane_id).first()
        ticket.seat_id = seat_.id
    else:
        return False
    db.session.commit()
    return True
