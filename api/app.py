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
    name = CharField()


class Restaurants(BaseModel):
    name = CharField()


class Tables(BaseModel):
    id_restaurant = ForeignKeyField(Restaurants, backref='Table')
    isOcupied = BooleanField()
    status = IntegerField()
    identify = IntegerField()


class Products(BaseModel):
    id_restaurant = IntegerField()
    name = CharField()
    price = FloatField()
    ingredients = CharField()
    picture = CharField()
    category = CharField()


class Orders(BaseModel):
    id_table = IntegerField()
    id_user = IntegerField()
    status = IntegerField()


class Order_Products(BaseModel):
    id_order = IntegerField()
    id_product = IntegerField()



@app.route('/')
def hello_world():
    user = Users.get_or_none(Users.name == 'Ioana')
    return user.email


@app.route('/product', methods=['GET'])
def get_menue():
    # id_restaurant = request.form['id_restaurant']
    for product in Products.select().where(Products.id_restaurant == 1):
        print(product.category)
    return 'bjhcdsa'

@app.route('/buy', methods=['POST'])
def buy():
    products = request.form['products']
    email = request.form['email']
    id_table = request.form['id_table']

    # products = '1, 3'
    # email = "ioanamoraru14@gmail.com"
    # id_table = "1"

    user = Users.get(Users.email == email)
    order = Orders.create(id_table=id_table, id_user=user.id, status=1)
    products = products.split(',')

    for product in products:
        Order_Products.create(id_product=product, id_order=order.id)

    return jsonify({
        'status': 'success',
        'message': 'You have successfully placed your order!'
    })



if __name__ == '__main__':
    app.run()
