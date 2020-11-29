from flask.blueprints import Blueprint
from flask import request
from service.get_airline import get_airline
from service.get_flight import get_flight

air_management = Blueprint('air', __name__, url_prefix='/air')


@air_management.route('/get_airline_api', methods=['POST'])
def get_airline_api():
    data = request.get_json(silent=True)
    start = data['start']
    destination = data['destination']
    airline_date = data['airline_date']
    if get_airline(start, destination, airline_date):
        return {'success': True}
    else:
        return {'success': False, 'info': '查询不到此航线信息'}


@air_management.route('/get_flight_api', methods=['POST'])
def get_flight_api():
    data = request.get_json(silent=True)
    start = data['start']
    destination = data['destination']
    airline_date = data['airline_date']
    flight_info = get_flight(start, destination, airline_date)
    return {'success': True, 'flight_info': flight_info}
