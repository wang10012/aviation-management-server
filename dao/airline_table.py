from global_var import db


class AirLine(db.Model):
    __tablename__ = 'AirLine'
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)

    start = db.Column(db.String(80), nullable=False)
    destination = db.Column(db.String(80), nullable=False)
    airline_date = db.Column(db.Date,nullable=False)
    mileage = db.Column(db.FLOAT)
    db.CheckConstraint('mileage > 0', name='check3')