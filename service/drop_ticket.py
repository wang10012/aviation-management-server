from dao.ticket_table import Ticket
from dao.seat_table import Seat
from global_var import db


def drop_ticket(choosed):
    for value in choosed:
        ticket = Ticket.query.filter_by(id=value).first()
        seat = Seat.query.filter_by(id=ticket.seat_id).first()
        db.session.delete(ticket)
        db.session.commit()
        db.session.delete(seat)
        db.session.commit()
    return True
