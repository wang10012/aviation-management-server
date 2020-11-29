from flask.blueprints import Blueprint
from flask import request
from service.book_ticket import book_ticket
from service.add_seat import add_seat
from service.check_is_seated import check_is_seated
from service.get_all_seats import get_all_seats
from service.get_ticket import get_ticket
from service.drop_ticket import drop_ticket
from service.is_ticketed import is_ticketed

ticket_management = Blueprint('ticket', __name__, url_prefix='/ticket')


@ticket_management.route('/book_ticket_api', methods=['POST'])
def book_ticket_api():
    data = request.get_json(silent=True)
    ticket_book_date = data['ticket_book_date'],
    ticket_standard_price = data['ticket_standard_price'],  # ticket_pay_price:还要写一个函数计算浮动
    ticket_class = data['ticket_class'],
    customer_username = data['customer_username'],
    flight_id = data['flight_id']
    if book_ticket(customer_username, flight_id, ticket_book_date, ticket_standard_price, ticket_class):
        return {'success': True, 'info': '订票成功！'}
    else:
        return {'success': False, 'info': '已经完成此航班订票/订票失败'}


@ticket_management.route('/add_seat_api', methods=['POST'])
def add_seat_api():
    data = request.get_json(silent=True)
    customer_username = data['customer_username']
    flight_id = data['flight_id']
    ticket_class = data['ticket_class']
    seat_code = data['seat_code']
    if add_seat(customer_username, flight_id, ticket_class, seat_code):
        return {'success': True, 'info': '选座成功！'}
    else:
        return {'success': False, 'info': '选座失败'}


# 没准不需要这个接口
@ticket_management.route('/check_is_seated_api', methods=['POST'])
def check_is_seated_api():
    data = request.get_json(silent=True)
    flight_id = data['flight_id']
    seat_code = data['seat_code']
    if check_is_seated(seat_code, flight_id):
        return {'success': True, 'info': '这个座位已经被选过了！'}
    else:
        return {'success': False, 'info': '这个座位是空的！'}


@ticket_management.route('/get_all_seats_api', methods=['POST'])
def get_all_seats_api():
    data = request.get_json(silent=True)
    flight_id = data['flight_id']
    seats_info = get_all_seats(flight_id)
    if seats_info:
        return {'success': True, 'seats_info': seats_info}
    else:
        return {'success': False, 'seats_info': '错误！'}

    # seat表重建，删库重建！！！
    # 订票后按钮禁用还没写！
    # add_seat中加一个插入ticket表的过程！!!


@ticket_management.route('/get_ticket_api', methods=['POST'])
def get_ticket_api():
    data = request.get_json(silent=True)
    username = data['username']
    tickets_info = get_ticket(username)
    # if tickets_info:
    #     return {'success': True, 'tickets_info': tickets_info}
    # else:
    #     return {'success': False, 'tickets_info': '错误！'}
    return {'success': True, 'tickets_info': tickets_info}


@ticket_management.route('/drop_ticket_api', methods=['POST'])
def drop_ticket_api():
    data = request.get_json(silent=True)
    choosed = data['choosed']
    if drop_ticket(choosed):
        return {'success': True, 'info': 'success'}
    else:
        return {'success': False, 'info': 'false'}


@ticket_management.route('/is_ticketed_api', methods=['POST'])
def is_ticketed_api():
    data = request.get_json(silent=True)
    customer_username = data['customer_username']
    flight_id = data['flight_id']
    if is_ticketed(customer_username, flight_id):
        return {'success': True, 'info': '已经订过了'}
    else:
        return {'success': False, 'info': '还没订'}
