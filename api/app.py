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
    id_table = request.form['id_restaurant']
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
        for product in Products.select().where(Products.restaurant == id_restaurant, Products.category == category):
            dict = {}
            dict['id'] = product.id
            dict['name'] = product.name
            dict['price'] = product.price
            auxList.append(dict)

        menu[category] = auxList

    return jsonify({
        'status': 'success',
        'data': menu
    })

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
    email = request.form['email']
    products = []
    user = Users.get_or_none(Users.email == email)

    order = Orders.get_or_none(Orders.user == user.id and Orders.status == 2)

    for order_product in Order_Products.select().where(Order_Products.order == order.id):
        produs = Products.get_or_none(Products.id == order_product.product)
        val = {'name': produs.name, 'price': produs.price}
        products.append(val)

    return jsonify({
        'status': 'success',
        'data': products
    })

@app.route('/orders', methods=['GET'])
def get_orders():
    #restaurat_id = request.form['restaurat_id']
    restaurat_id = 1

    orders = []
    for order in Tables.select(Tables.id).where(Tables.restaurant==restaurat_id):
        print(order.identify)
    return ""

if __name__ == '__main__':
    app.run(host="0.0.0.0")
