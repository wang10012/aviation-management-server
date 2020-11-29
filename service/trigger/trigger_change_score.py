from dao.airline_table import AirLine
from dao.flight_table import Flight
from dao.vip_customer_table import VIPCustomer
from dao.ticket_table import Ticket
from global_var import db
from service.is_vip import is_vip


@db.event.listens_for(Ticket, 'after_insert')
def trigger_add_score(mapper, connection, target):
    vipcustomer_table = VIPCustomer.__table__
    if is_vip(target.customer_username):
        flight = Flight.query.filter_by(id=target.flight_id).first()
        airline = AirLine.query.filter_by(id=flight.air_line_id).first()
        vipcustomer = VIPCustomer.query.filter_by(username=target.customer_username).first()
        if vipcustomer.score + airline.mileage > 2000:
            cls = 'VIP3'
        elif vipcustomer.score + airline.mileage > 1000:
            cls = 'VIP2'
        else:
            cls = vipcustomer.VIP_class
        connection.execute(
            vipcustomer_table.update().where(vipcustomer_table.c.username == target.customer_username).
                values(score=vipcustomer.score + airline.mileage, VIP_class=cls)
        )


@db.event.listens_for(Ticket, 'after_delete')
def trigger_subtract_score(mapper, connection, target):
    vipcustomer_table = VIPCustomer.__table__
    if is_vip(target.customer_username):
        flight = Flight.query.filter_by(id=target.flight_id).first()
        airline = AirLine.query.filter_by(id=flight.air_line_id).first()
        vipcustomer = VIPCustomer.query.filter_by(username=target.customer_username).first()
        if vipcustomer.score - airline.mileage > 2000:
            cls = 'VIP3'
        elif vipcustomer.score - airline.mileage > 1000:
            cls = 'VIP2'
        else:
            cls = 'VIP1'
        connection.execute(
            vipcustomer_table.update().where(vipcustomer_table.c.username == target.customer_username).
                values(score=vipcustomer.score - airline.mileage, VIP_class=cls)
        )
