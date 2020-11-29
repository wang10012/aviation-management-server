from dao.ticket_table import Ticket
from dao.vip_customer_table import VIPCustomer
from utils.calc_vip_price import calc_vip_price
from global_var import db
from service.is_vip import is_vip


def book_ticket(customer_username, flight_id, ticket_book_date, ticket_standard_price, ticket_class):
    ticket = Ticket.query.filter_by(customer_username=customer_username,
                                    flight_id=flight_id).first()
    if not ticket:
        if is_vip(customer_username):
            vipcustomer = VIPCustomer.query.filter_by(username=customer_username).first()
            vip_class = vipcustomer.VIP_class
            ticket = Ticket(
                ticket_book_date=ticket_book_date,
                ticket_pay_price=calc_vip_price(vip_class, ticket_standard_price),
                ticket_class=ticket_class,
                customer_username=customer_username,
                flight_id=flight_id
            )
            db.session.add(ticket)
        else:
            ticket = Ticket(
                ticket_book_date=ticket_book_date,
                ticket_pay_price=ticket_standard_price,
                ticket_class=ticket_class,
                customer_username=customer_username,
                flight_id=flight_id
            )
            db.session.add(ticket)
    else:
        return False
    db.session.commit()
    return True
