from global_var import db


class AircompanyPlane(db.Model):
    __tablename__ = 'AircompanyPlane'

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)

    air_company_name = db.Column(db.String(80), db.ForeignKey('AirCompany.name'))
    plane_id = db.Column(db.String(20), db.ForeignKey('Plane.id'))
