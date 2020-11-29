from global_var import db


class Flight(db.Model):
    __tablename__ = 'Flight'
    id = db.Column(db.String(20), primary_key=True)

    start_time = db.Column(db.Time, nullable=False)
    arrive_time = db.Column(db.Time, nullable=False)
    first_class_price = db.Column(db.FLOAT, nullable=False)
    business_class_price = db.Column(db.FLOAT, nullable=False)
    economy_class_price = db.Column(db.FLOAT, nullable=False)

    num_remain_seat = db.Column(db.Integer)
    num_remain_first_class = db.Column(db.Integer)
    num_remain_business_class = db.Column(db.Integer)
    num_remain_economy_class = db.Column(db.Integer)

    air_line_id = db.Column(db.Integer, db.ForeignKey('AirLine.id'))
    airport_id = db.Column(db.Integer, db.ForeignKey("Airport.id"))
    plane_id = db.Column(db.String(20), db.ForeignKey('Plane.id'))
    air_company_name = db.Column(db.String(80), db.ForeignKey('AirCompany.name'))

    db.CheckConstraint('num_remain_seat > 0', name='check4')
    db.CheckConstraint('num_remain_first_class > 0', name='check5')
    db.CheckConstraint('num_remain_business_class > 0', name='check6')
    db.CheckConstraint('num_remain_economy_class > 0', name='check7')
