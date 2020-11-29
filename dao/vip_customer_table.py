from global_var import db


# 弱实体
class VIPCustomer(db.Model):
    __tablename__ = 'VIPCustomer'
    username = db.Column(db.String(32), primary_key=True)

    VIP_class = db.Column(db.String(20), default="VIP1")
    score = db.Column(db.Integer, default=0)
