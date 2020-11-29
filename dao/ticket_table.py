from global_var import db


class Ticket(db.Model):
    __tablename__ = 'Ticket'
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)

    ticket_book_date = db.Column(db.Date, nullable=False)
    ticket_pay_price = db.Column(db.FLOAT)
    ticket_class = db.Column(db.String(20), nullable=False)

    flight_id = db.Column(db.String(20), db.ForeignKey('Flight.id'))
    customer_username = db.Column(db.String(32), db.ForeignKey("Customer.username"))
    seat_id = db.Column(db.Integer, db.ForeignKey("Seat.id"))


