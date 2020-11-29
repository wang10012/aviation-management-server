import os

HOST = '127.0.0.1'
PASSWORD = ''
PORT = '3306'
DATABASE = 'wsj_air'
USERNAME = 'root'

DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=USERNAME,
                                                                                        password=PASSWORD, host=HOST,
                                                                                        port=PORT, db=DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True
SESSION_TYPE = 'filesystem'
SECRET_KEY = os.urandom(128)
