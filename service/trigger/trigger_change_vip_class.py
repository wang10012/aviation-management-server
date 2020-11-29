from global_var import db
from dao.vip_customer_table import VIPCustomer


# 具体数值后面再改
# @db.event.listens_for(VIPCustomer.score, 'set', propagate=True)
# def trigger_change_vip_class(target, value, oldvalue, initiator):
#     vipcustomer = VIPCustomer.query.filter_by(username=target.username).first()
#     if value >= 1000:
#         vipcustomer.VIP_class == 'VIP2'
#     elif value >= 2000:
#         vipcustomer.VIP_class == 'VIP3'
from service.is_vip import is_vip


# @db.event.listens_for(VIPCustomer, 'before_update')
# def trigger_change_vip_class(mapper, connection, target):
#     if target.score >= 2000:
#         target.Vip_class = 'VIP3'
#     elif target.score >= 1000:
#         target.Vip_class = 'VIP2'
    # vipcustomer_table = VIPCustomer.__table__
    # if is_vip(target.customer_username):
    #     flight = Flight.query.filter_by(id=target.flight_id).first()
    #     airline = AirLine.query.filter_by(id=flight.air_line_id).first()
    #     vipcustomer = VIPCustomer.query.filter_by(username=target.customer_username).first()
    #     connection.execute(
    #         vipcustomer_table.update().where(vipcustomer_table.c.username == target.customer_username).
    #             values(score=vipcustomer.score + airline.mileage)
    #     )
