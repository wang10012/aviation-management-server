from flask.blueprints import Blueprint
from flask import request
from service.login import customer_login
from service.add_customer import add_customer
from service.complete_per_info import complete_per_info
from service.get_customer_info import get_customer_info
from service.get_vip_info import get_vip_info
from service.is_vip import is_vip
from service.set_vip import set_vip
from service.is_completed_per_info import is_completed_per_info
from typing import *

customer_management = Blueprint('customer', __name__, url_prefix='/customer')


@customer_management.route('/login', methods=['POST'])
def login():
    data = request.get_json(silent=True)
    username = data['username']
    password = data['password']
    if customer_login(username, password):
        return {'success': True, 'info': '客户登录成功'}
    else:
        return {'success': False, 'info': '您的账号或密码有错误'}


@customer_management.route('/add_customer_api', methods=['POST'])
def add_customer_api():
    data = request.get_json(silent=True)
    name = data['name']
    username = data['username']
    password = data['password']
    phone_number = data['phone_number']
    if add_customer(name, username, password, phone_number):
        return {'success': True, 'info': 'success!'}
    else:
        return {'success': False, 'info': '用户名已经存在'}


@customer_management.route('get_customer_info_api', methods=['POST'])
def get_customer_info_api():
    data = request.get_json(silent=True)
    username = data['username']
    if get_customer_info(username):
        customer_info: Dict[str, str] = get_customer_info(username)
        return {'success': True, 'customer_info': customer_info}
    else:
        return {'success': False}


@customer_management.route('/complete_per_info_api', methods=['POST'])
def complete_per_info_api():
    data = request.get_json(silent=True)
    username = data['username']
    age = data['age']
    gender = data['gender']
    ID_number = data['ID_number']
    if complete_per_info(username, age, gender, ID_number):
        return {'success': True, 'info': 'success!'}
    else:
        return {'success': False, 'info': '不可能错误！'}


@customer_management.route('/get_vip_info_api', methods=['POST'])
def get_vip_info_api():
    data = request.get_json(silent=True)
    username = data['username']
    if get_vip_info(username):
        vip_customer_info: Dict[str, str] = get_vip_info(username)
        return {'success': True, 'vip_customer_info': vip_customer_info}
    else:
        return {'success': False}


@customer_management.route('/is_vip_api', methods=['POST'])
def is_vip_api():
    data = request.get_json(silent=True)
    username = data['username']
    if is_vip(username):
        return {'success': True, 'info': 'success!'}
    else:
        return {'success': False, 'info': 'false！'}


@customer_management.route('/set_vip_api', methods=['POST'])
def set_vip_api():
    data = request.get_json(silent=True)
    username = data['username']
    if set_vip(username):
        return {'success': True, 'info': 'success!'}
    else:
        return {'success': False, 'info': 'false！'}


@customer_management.route('/is_completed_per_info_api', methods=['POST'])
def is_completed_per_info_api():
    data = request.get_json(silent=True)
    username = data['customer_username']
    if is_completed_per_info(username):
        return {'success': True, 'info': 'success!'}
    else:
        return {'success': False, 'info': 'false！'}
