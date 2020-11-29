from dao.vip_customer_table import VIPCustomer
from typing import *


def get_vip_info(customer_username):
    vipcustomer = VIPCustomer.query.filter_by(username=customer_username).first()
    result: Dict[str] = {
        'username': vipcustomer.username,
        'VIP_class': vipcustomer.VIP_class,
        'score': str(vipcustomer.score)  # 需要str化吗？？
    }
    return result
