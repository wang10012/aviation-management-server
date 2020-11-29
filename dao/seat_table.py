from global_var import db


class Seat(db.Model):
    __tablename__ = 'Seat'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    seat_code = db.Column(db.Integer)
    seat_type = db.Column(db.String(20))

    plane_id = db.Column(db.String(20), db.ForeignKey('Plane.id'))
