from dao.ticket_table import Ticket


def is_ticketed(customer_username, flight_id):
    ticket = Ticket.query.filter_by(customer_username=customer_username,
                                    flight_id=flight_id).first()
    if not ticket:
        return False
    return True
