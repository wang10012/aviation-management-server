from dao.airport_table import Airport
from global_var import db


def add_airport_info(start_name, arrive_name):
    airport = Airport.query.filter_by(start_name=start_name, arrive_name=arrive_name).first()
    if not airport:
        airport = Airport(
            start_name=start_name,
            arrive_name=arrive_name,
        )
        db.session.add(airport)
    else:
        return False
    db.session.commit()
    return True
