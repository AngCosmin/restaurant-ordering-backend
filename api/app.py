from peewee import CharField, Model, MySQLDatabase
from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

MYSQL_DB = 'app'
MYSQL_HOST = 'db'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PASS = 'root'

db = MySQLDatabase(MYSQL_DB, host=MYSQL_HOST, port=MYSQL_PORT, user=MYSQL_USER, passwd=MYSQL_PASS)
db.connect()

class BaseModel(Model):
    class Meta:
        database = db


class Users(BaseModel):
    username = CharField()
    password = CharField()


@app.route('/')
def hello_world():
    user = Users.get_or_none(Users.username == 'Cosmin')
    return user.password

    # return 'Hello World!'


if __name__ == '__main__':
    app.run()
