from dao.airport_table import Airport
from global_var import db


def delete_airport_info(airport_id):
    airport = Airport.query.filter_by(id=airport_id).first()
    if airport:
        db.session.delete(airport)
    else:
        return False
    db.session.commit()
    return True

