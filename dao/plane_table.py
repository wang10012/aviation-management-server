from global_var import db


class Plane(db.Model):
    __tablename__ = 'Plane'
    id = db.Column(db.String(20), primary_key=True)  # 飞机型号

    num_seat = db.Column(db.Integer, nullable=False)
    num_first_class_seat = db.Column(db.Integer, nullable=False)
    num_business_class_seat = db.Column(db.Integer, nullable=False)
    num_economy_class_seat = db.Column(db.Integer, nullable=False)

    db.CheckConstraint('num_first_class + num_tourist_class == num_seat', name='check1')
