from peewee import CharField, IntegerField, FloatField, BooleanField, ForeignKeyField, Model, MySQLDatabase
from flask import Flask
from flask import request, jsonify

app = Flask(__name__)
app.config['DEBUG'] = True

MYSQL_DB = 'app'
MYSQL_HOST = 'localhost'
MYSQL_PORT = 6000
MYSQL_USER = 'root'
MYSQL_PASS = 'root'

db = MySQLDatabase(MYSQL_DB, host=MYSQL_HOST, port=MYSQL_PORT, user=MYSQL_USER, passwd=MYSQL_PASS)
db.connect()


class BaseModel(Model):
    class Meta:
        database = db


class Users(BaseModel):
    email = CharField()
    username = CharField()


class Restaurants(BaseModel):
    name = CharField()


class Tables(BaseModel):
    id_restaurant = ForeignKeyField(Restaurants, backref='table')
    isOcupied = BooleanField()
    status = IntegerField()
    identify = IntegerField()


class Products(BaseModel):
    id_restaurant = ForeignKeyField(Restaurants, backref='product')
    name = CharField()
    price = FloatField()
    ingredients = CharField()
    picture = CharField()
    category = CharField()


class Orders(BaseModel):
    id_table = ForeignKeyField(Tables, backref='Command')
    id_user = ForeignKeyField(Users, backref='Command')
    status = IntegerField()


class Order_Products(BaseModel):
    id_order = IntegerField()
    id_product = IntegerField()



@app.route('/')
def hello_world():
    user = Users.get_or_none(Users.username == 'Ioana')
    return user.password









if __name__ == '__main__':
    app.run()
