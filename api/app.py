from peewee import CharField, IntegerField, FloatField, BooleanField, ForeignKeyField, Model, MySQLDatabase
from flask import Flask
from flask import request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config['DEBUG'] = True

cors = CORS(app)

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
    email = CharField()
    password = CharField()


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


class Reviews(BaseModel):
    product = ForeignKeyField(Products, backref='Table')
    value = FloatField()


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


def get_rating(id_product):
    sum = 0
    nr = 0
    for review in Reviews.select().where(Reviews.product == id_product):
        sum += review.value
        nr += 1

    if nr == 0:
        return ''

    value = sum / nr
    return value


@app.route('/product', methods=['GET'])
def get_menu():
    id_table = request.args['id_table']
    if 'category' in request.args:
        base_category = request.args['category']
    else:
        base_category = None

    query = Tables.update(isOcupied=True).where(Tables.id == id_table)
    query.execute()

    id_restaurant = Tables.get(Tables.id == id_table).restaurant
    categories = []
    for product in Products.select().where(Products.restaurant == id_restaurant):
        categories.append(product.category)

    if base_category is not None:
        categories = [base_category]
    else:
        categories = list(set(categories))
    menu = []
    for category in categories:
        for product in Products.select().where(Products.restaurant == id_restaurant, Products.category == category):
            dict = {}
            dict['id'] = product.id
            dict['name'] = product.name
            dict['price'] = product.price
            dict['picture'] = product.picture
            dict['category'] = category
            rating = get_rating(product.id)
            dict['rating'] = rating
            menu.append(dict)

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


@app.route('/categories', methods=['GET'])
def get_categories():
    if 'id_table' in request.args:
        id_table = request.args['id_table']
        id_restaurant = Tables.get(Tables.id == id_table).restaurant
    else:
        id_restaurant = None

    if id_restaurant is not None:
        categories = []
        for product in Products.select().where(Products.restaurant == id_restaurant):
            categories.append(product.category)
        categories = list(set(categories))
    else:
        categories = []
        for restaurant in Restaurants.select():
            for product in Products.select().where(Products.restaurant == restaurant.id):
                categories.append(product.category)
        categories = list(set(categories))

    return jsonify({
        'status': 'success',
        'data': categories
    })


@app.route('/orders', methods=['GET'])
def get_orders():
    restaurat_id = request.args['restaurat_id']

    ord = []
    for tables in Tables.select().where(Tables.restaurant == restaurat_id):
        prod = []
        for orders in Orders.select().where(Orders.table==tables.id, Orders.status == 1):

            for product_ids in Order_Products.select().where(Order_Products.order==orders.id):

                for products in Products.select().where(Products.id==product_ids.product):
                    prod.append(products.name)
        if prod != []:
            ord.append({'table_id': tables.id, 'products': prod})

    return jsonify({
        'status': 'success',
        'data': ord
    })

@app.route('/add_product', methods=['POST'])
def add_product():
    id_restaurant = request.form['restaurant_id']
    name = request.form['name']
    price = request.form['price']
    ingredients = request.form['ingredients']
    category = request.form['category']

    Products.create(restaurant=id_restaurant, name=name, price=price, ingredients=ingredients, category=category)


    return jsonify({
        'status': 'success',
        'message': 'You have successfully placed your product!'
    })

@app.route('/add_rating', methods=['POST'])
def add_rating():
    id_product = request.form['product_id']
    rating = request.form['rating']

    Reviews.create(product=id_product, value=rating)

    return jsonify({
        'status': 'success',
        'message': 'You have successfully placed your review!'
    })


<<<<<<< HEAD
@app.route('/get_rating', methods=['GET'])
def get_rating():
    id_product = request.args['product_id']
    sum = 0
    nr = 0
    for review in Reviews.select().where(Reviews.product == id_product):
        sum += review.value
        nr += 1

    value = sum / nr

    return jsonify({
        'status': 'success',
        'data': value
    })



@app.route('/restaurant/login', methods=['POST'])
def restaurant_login():
    email = request.json['email']
    password = request.json['password']

    restaurant = Restaurants.get(Restaurants.email == email)
    if restaurant.password == password:
        return jsonify({
            'success': True,
            'message': 'You have successfully log in!'
        })
    else:
        return '', 400

@app.route('/restaurant/products', methods=['GET'])
def restaurant_products():
    id_restaurant = request.form['restaurant_id']

    restaurant = Restaurants.get(Restaurants.id == id_restaurant)
    products = []
    for product in Products.select().where(Products.restaurant == restaurant.id):
        dict = {}
        dict['name'] = product.name
        dict['rating'] = get_rating(product.id)
        nr = 0
        for review in Reviews.select().where(Reviews.product == product.id):
            nr += 1
        dict['persons'] = nr
        products.append(dict)

    return jsonify({
        'status': 'success',
        'data': products
    })


if __name__ == '__main__':
    app.run()

