from global_var import db


class Customer(db.Model):
    __tablename__ = 'Customer'
    username = db.Column(db.String(32), primary_key=True)

    name = db.Column(db.String(32), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(20))
    ID_number = db.Column(db.String(80), unique=True)
    type = db.Column(db.String(20), default="NO-VIP")

