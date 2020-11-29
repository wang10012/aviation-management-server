from flask_sqlalchemy import SQLAlchemy
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
import config

db = SQLAlchemy()
s = Serializer(config.SECRET_KEY, expires_in=3600)