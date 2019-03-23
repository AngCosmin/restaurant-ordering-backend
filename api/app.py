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
    restaurant = ForeignKeyField(Restaurants, backref='Table')
    isOcupied = BooleanField()
    status = IntegerField()
    identify = CharField()


class Products(BaseModel):
    restaurant = ForeignKeyField(Restaurants, backref='Table')
    name = CharField()
    price = FloatField()
    ingredients = CharField()
    picture = CharField()
    category = CharField()


class Orders(BaseModel):
    table = ForeignKeyField(Tables, backref='Order')
    user = ForeignKeyField(Users, backref='Order')
    status = IntegerField()


class Order_Products(BaseModel):
    order = ForeignKeyField(Orders, backref='Order')
    product = ForeignKeyField(Products, backref='Order')


@app.route('/')
def hello_world():
    user = Users.get_or_none(Users.name == 'Ioana')
    return user.email


@app.route('/product', methods=['GET'])
def get_menu():
    id_table = 1  # request.form['id_restaurant']
    query = Tables.update(isOcupied=True).where(Tables.id == id_table)
    query.execute()

    id_restaurant = Tables.get(Tables.id == id_table).restaurant
    categories = []
    for product in Products.select().where(Products.restaurant == id_restaurant):
        categories.append(product.category)

    categories = list(set(categories))
    menu = {}
    for category in categories:
        auxList = []
        for product in Products.select().where(
                Products.restaurant == id_restaurant and Products.category == category):
            dict = {}
            dict['id'] = product.id
            dict['name'] = product.name
            dict['price'] = product.price
            auxList.append(dict)

        menu[category] = auxList

    return 'bjhcdsa'

@app.route('/buy', methods=['POST'])
def buy():
    products = request.form['products']
    email = request.form['email']
    id_table = request.form['table_id']

    # products = '1, 3'
    # email = "ioanamoraru14@gmail.com"
    # id_table = "1"

    user = Users.get(Users.email == email)
    order = Orders.create(table=id_table, user=user.id, status=1)
    products = products.split(',')

    for product in products:
        Order_Products.create(product=product, order=order.id)

    return jsonify({
        'status': 'success',
        'message': 'You have successfully placed your order!'
    })


@app.route('/bill', methods=['GET'])
def get_bill():
    email = 'cosminzorr@gmail.com'  # request.form['email']
    products = []

    user = Users.get_or_none(Users.email == email)

    return user.name


if __name__ == '__main__':
    app.run()
