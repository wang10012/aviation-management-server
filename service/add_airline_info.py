from dao.airline_table import AirLine
from global_var import db


# useless
def add_airline_info(start, destination, airline_date, mileage):
    airline = AirLine.query.filter_by(start=start, destination=destination,
                                      airline_date=airline_date, mileage=mileage).first()
    if not airline:
        airline = AirLine(
            start=start,
            destination=destination,
            airline_date=airline_date,
            mileage=mileage
        )
        db.session.add(airline)
    else:
        return False
    db.session.commit()
    return True
