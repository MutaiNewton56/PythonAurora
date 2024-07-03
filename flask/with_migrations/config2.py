import os

basedir=os.path.abspath(os.path.dirname(__file__))

print(basedir)
class Config2:
    SQLALCHEMY_DATABASE_URI="sqlite:///"+os.path.join(basedir,'dbs/db.db')
