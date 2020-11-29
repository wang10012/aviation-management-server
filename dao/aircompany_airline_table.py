from global_var import db


class AircompanyAirline(db.Model):
    __tablename__ = 'AircompanyAirline'
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)

    air_company_name = db.Column(db.String(80), db.ForeignKey('AirCompany.name'))
    air_line_id = db.Column(db.Integer, db.ForeignKey('AirLine.id'))
