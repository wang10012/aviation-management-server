from global_var import db


class Airport(db.Model):
    __tablename__ = 'Airport'
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)

    start_name = db.Column(db.String(50), nullable=False)
    arrive_name = db.Column(db.String(50), nullable=False)


