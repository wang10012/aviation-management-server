from dao.flight_table import Flight
from global_var import db


def delete_flight_info(flight_id):
    flight = Flight.query.filter_by(id=flight_id).first()
    if flight:
        db.session.delete(flight)
    else:
        return False
    db.session.commit()
    return True

