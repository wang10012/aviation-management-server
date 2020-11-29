from dao.airline_table import AirLine


# 判断根据起始地，目的地，航线日期，该航线是否存在
def get_airline(start, destination, airline_date):
    return bool(AirLine.query.filter_by(start=start, destination=destination, airline_date=airline_date).first())
