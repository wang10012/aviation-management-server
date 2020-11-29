def calc_vip_price(vip_class, ticket_standard_price):
    ticket_price = 0
    ticket_standard_price, = ticket_standard_price
    if vip_class == 'VIP1':
        ticket_price = ticket_standard_price * 0.9
    elif vip_class == 'VIP2':
        ticket_price = ticket_standard_price * 0.85
    elif vip_class == 'VIP3':
        ticket_price = ticket_standard_price * 0.8
    return ticket_price
