from global_var import db


class AirCompany(db.Model):
    __tablename__ = 'AirCompany'
    name = db.Column(db.String(80), primary_key=True)
    password = db.Column(db.String(128), nullable=False)
    call_number = db.Column(db.Integer)
