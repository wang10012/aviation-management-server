from flask.blueprints import Blueprint
from flask import request
from service.login import admin_login
from service.add_company import add_company
from service.get_company_info import get_company_info
from service.complete_company_info import complete_company_info
from service.add_company_plane_info import add_company_plane_info
from service.get_company_plane_info import get_company_plane_info
from service.delete_company_plane_info import delete_company_plane_info
from service.add_airport_info import add_airport_info
from service.get_airport_info import get_airport_info
from service.delete_airport_info import delete_airport_info
from service.add_company_airline_info import add_company_airline_info
from service.add_flight_info import add_flight_info
from service.get_company_airline_info import get_company_airline_info
from service.get_plane_info import get_plane_info
from service.get_company_flight_infos import get_company_flight_infos
from service.delete_company_airline_info import delete_company_airline_info
from service.delete_flight_info import delete_flight_info
from typing import *

admin_management = Blueprint('admin', __name__, url_prefix='/admin')


@admin_management.route('/admin_login_api', methods=['POST'])
def admin_login_api():
    data = request.get_json(silent=True)
    name = data['name']
    password = data['password']
    if admin_login(name, password):
        return {'success': True, 'info': '管理员登录成功'}
    else:
        return {'success': False, 'info': '您的账号或密码有错误'}


@admin_management.route('/add_company_api', methods=['POST'])
def add_company_api():
    data = request.get_json(silent=True)
    name = data['company_name']
    password = data['company_password']
    if add_company(name, password):
        return {'success': True, 'info': 'success!'}
    else:
        return {'success': False, 'info': '公司名已经存在'}


@admin_management.route('/get_company_info_api', methods=['POST'])
def get_company_info_api():
    data = request.get_json(silent=True)
    name = data['company_name']
    if get_company_info(name):
        company_info: Dict[str, str] = get_company_info(name)
        return {'success': True, 'company_info': company_info}
    else:
        return {'company_info': {'得不到信息！'}}


@admin_management.route('/complete_company_info_api', methods=['POST'])
def complete_company_info_api():
    data = request.get_json(silent=True)
    company_name = data['company_name']
    company_password = data['company_password']
    call_number = data['call_number']
    if complete_company_info(company_name, company_password, call_number):
        return {'success': True, 'info': 'success!'}
    else:
        return {'info': '不可能错误！'}


@admin_management.route('/add_company_plane_info_api', methods=['POST'])
def add_company_plane_info_api():
    data = request.get_json(silent=True)
    company_name = data['company_name']
    plane_id = data['plane_id']
    if add_company_plane_info(company_name, plane_id):
        return {'success': True, 'info': 'success!'}
    else:
        return {'info': '此航空公司已经添加过飞机信息了'}


@admin_management.route('/get_company_plane_info_api', methods=['POST'])
def get_company_plane_info_api():
    data = request.get_json(silent=True)
    company_name = data['company_name']
    company_plane_infos = get_company_plane_info(company_name)
    return {'success': True, 'company_plane_infos': company_plane_infos}


@admin_management.route('/delete_company_plane_info_api', methods=['POST'])
def delete_company_plane_info_api():
    data = request.get_json(silent=True)
    company_plane_id = data['company_plane_id']
    try:
        if delete_company_plane_info(company_plane_id):
            return {'success': True, 'info': '删除飞机成功！'}
    except Exception as ignore:
        return {'success': False, 'info': '删除失败!'}


@admin_management.route('/add_airport_info_api', methods=['POST'])
def add_airport_info_api():
    data = request.get_json(silent=True)
    start_name = data['start_name']
    arrive_name = data['arrive_name']
    if add_airport_info(start_name, arrive_name):
        return {'success': True, 'info': 'success!'}
    else:
        return {'info': '此航空公司已经添加过机场信息了'}


@admin_management.route('/get_airport_info_api', methods=['POST'])
def get_airport_info_api():
    data = request.get_json(silent=True)
    airport_infos = get_airport_info()
    return {'success': True, 'airport_infos': airport_infos}


@admin_management.route('/delete_airport_info_api', methods=['POST'])
def delete_airport_info_api():
    data = request.get_json(silent=True)
    airport_id = data['airport_id']
    try:
        if delete_airport_info(airport_id):
            return {'success': True, 'info': '删除机场成功！'}
    except Exception as ignore:
        return {'success': False, 'info': '删除失败!'}


@admin_management.route('/add_company_airline_info_api', methods=['POST'])
def add_company_airline_info_api():
    data = request.get_json(silent=True)
    company_name = data['company_name']
    airline_id = data['airline_id']
    if add_company_airline_info(company_name, airline_id):
        return {'success': True, 'info': 'success!'}
    else:
        return {'info': '此航空公司已经添加过航线信息了'}


@admin_management.route('/add_flight_info_api', methods=['POST'])
def add_flight_info_api():
    data = request.get_json(silent=True)
    flight_id = data['flight_id']
    start_time = data['start_time']
    arrive_time = data['arrive_time']
    first_class_price = data['first_class_price']
    business_class_price = data['business_class_price']
    economy_class_price = data['economy_class_price']
    num_remain_seat = data['num_remain_seat']
    num_remain_first_class = data['num_remain_first_class']
    num_remain_business_class = data['num_remain_business_class']
    num_remain_economy_class = data['num_remain_economy_class']
    air_line_id = data['air_line_id']
    airport_id = data['airport_id']
    plane_id = data['plane_id']
    company_name = data['company_name']
    try:
        if add_flight_info(flight_id, start_time, arrive_time, first_class_price, business_class_price,
                           economy_class_price, num_remain_seat, num_remain_first_class,
                           num_remain_business_class, num_remain_economy_class, air_line_id, airport_id, plane_id,
                           company_name):
            return {'success': True, 'info': 'success!'}
    except Exception as ignore:
        return {'success': False, 'info': '此航空公司已经添加过航班信息了!'}


@admin_management.route('/get_company_airline_info_api', methods=['POST'])
def get_company_airline_info_api():
    data = request.get_json(silent=True)
    company_name = data['company_name']
    company_airline_infos = get_company_airline_info(company_name)
    return {'success': True, 'company_airline_infos': company_airline_infos}


@admin_management.route('/get_plane_info_api', methods=['POST'])
def get_plane_info_api():
    data = request.get_json(silent=True)
    plane_id = data['plane_id']
    plane_infos = get_plane_info(plane_id)
    return {'success': True, 'plane_infos': plane_infos}


@admin_management.route('/get_company_flight_infos_api', methods=['POST'])
def get_company_flight_infos_api():
    data = request.get_json(silent=True)
    company_name = data['company_name']
    flight_infos = get_company_flight_infos(company_name)
    return {'success': True, 'flight_infos': flight_infos}


@admin_management.route('/delete_company_airline_info_api', methods=['POST'])
def delete_company_airline_info_api():
    data = request.get_json(silent=True)
    company_airline_id = data['company_airline_id']
    try:
        if delete_company_airline_info(company_airline_id):
            return {'success': True, 'info': '删除航线成功！'}
    except Exception as ignore:
        return {'success': False, 'info': '删除失败!'}


@admin_management.route('/delete_flight_info_api', methods=['POST'])
def delete_flight_info_api():
    data = request.get_json(silent=True)
    plane_id = data['flight_id']
    try:
        if delete_flight_info(plane_id):
            return {'success': True, 'info': '删除航班成功！'}
    except Exception as ignore:
        return {'success': False, 'info': '删除失败!'}
