import os
sqlite = False

basedir = os.path.abspath(os.path.dirname(__file__))
if sqlite:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db') #For sqlite
else:
    DB_USER = "root"
    DB_PASSWORD = "ubuntu"
    DB_HOST = "127.0.0.1"
    DB_NAME = "gobidb"

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://"+DB_USER+":"+DB_PASSWORD+"@"+DB_HOST+"/"+DB_NAME #For mysql

