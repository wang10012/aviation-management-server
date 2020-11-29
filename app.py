from flask import Flask
from flask_cors import CORS
from global_var import db
import config

from dao.air_company_table import AirCompany
from dao.airport_table import Airport
from dao.customer_table import Customer
from dao.seat_table import Seat
from dao.vip_customer_table import VIPCustomer
from dao.aircompany_airline_table import AircompanyAirline
from dao.aircompany_plane_table import AircompanyPlane

from api.customer_management import customer_management
from api.air_management import air_management
from api.ticket_management import ticket_management
from api.admin_management import admin_management

app = Flask(__name__)
app.config.from_object(config)
CORS(app, resources=r'/*', supports_credentials=True)


def init():
    import service.trigger.trigger_change_score
    import service.trigger.trigger_change_vip_class
    import service.trigger.trigger_set_num_remain_seat
    app.register_blueprint(customer_management)
    app.register_blueprint(air_management)
    app.register_blueprint(ticket_management)
    app.register_blueprint(admin_management)


init()

with app.app_context():
    db.init_app(app=app)
    # db.drop_all()
    db.create_all()

if __name__ == '__main__':
    app.run()
