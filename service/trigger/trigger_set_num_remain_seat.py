from dao.ticket_table import Ticket
from dao.flight_table import Flight
from global_var import db


@db.event.listens_for(Ticket, 'after_insert')
def trigger_set_num_remain_seat(mapper, connection, target):
    flight_table = Flight.__table__
    flight = Flight.query.filter_by(id=target.flight_id).first()
    if target.ticket_class[0] == '经济舱':
        connection.execute(
            flight_table.update().where(flight_table.c.id == target.flight_id).
                values(num_remain_seat=flight.num_remain_seat - 1, num_remain_economy_class=
                    flight.num_remain_economy_class - 1)
        )
    elif target.ticket_class[0] == '商务舱':
        connection.execute(
            flight_table.update().where(flight_table.c.id == target.flight_id).
                values(num_remain_seat=flight.num_remain_seat - 1, num_remain_business_class=
            flight.num_remain_business_class - 1)
        )
    elif target.ticket_class[0] == '头等舱':
        connection.execute(
            flight_table.update().where(flight_table.c.id == target.flight_id).
                values(num_remain_seat=flight.num_remain_seat - 1, num_remain_first_class=
            flight.num_remain_first_class - 1)
        )

# 1. 增加对应三个等级舱位的数量更新触发器
# 2. 在Flight表中增加对应属性：三种舱位对应数量
# 3. 设置4个flag来判断票数是否为0，是的话用v-if把对应按钮化为disable
# 4. 已经购买过（在ticket表中），不管是哪一种舱位，直接把总选购按钮disable：但和卖票换成的按钮不同！
# 5. 对总选购标签加一个flag（当个人信息补全的时候，则可用，否则弹窗：给出对应路由去补全个人信息。），
#    created时就检测flag。

# 重要！！！！ticket_class返回值错误！，返回了（某某， ）


@db.event.listens_for(Ticket, 'after_delete')
def trigger_set_num_remain_seat(mapper, connection, target):
    flight_table = Flight.__table__
    flight = Flight.query.filter_by(id=target.flight_id).first()
    if target.ticket_class == '经济舱':
        connection.execute(
            flight_table.update().where(flight_table.c.id == target.flight_id).
                values(num_remain_seat=flight.num_remain_seat + 1, num_remain_economy_class=
                    flight.num_remain_economy_class + 1)
        )
    elif target.ticket_class == '商务舱':
        connection.execute(
            flight_table.update().where(flight_table.c.id == target.flight_id).
                values(num_remain_seat=flight.num_remain_seat + 1, num_remain_business_class=
            flight.num_remain_business_class + 1)
        )
    elif target.ticket_class == '头等舱':
        connection.execute(
            flight_table.update().where(flight_table.c.id == target.flight_id).
                values(num_remain_seat=flight.num_remain_seat + 1, num_remain_first_class=
            flight.num_remain_first_class + 1)
        )
