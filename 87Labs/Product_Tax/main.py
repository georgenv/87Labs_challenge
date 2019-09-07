from flask import jsonify, request
from bson.json_util import dumps
from app import app, mongo


def calculate_tax(product):
    """
    Calculate impost on a product

    Params:
        product (dict): dictionary containing product attributes

    Returns:
        tax (float): float number representing the impost's value
    """

    tax = 0
    volume = product['height'] * product['width'] * product['length']
    calculated_weight = volume * 300

    if calculated_weight <= 100:
        tax = round(0.05 * product['price'], 2)
    else:
        tax = round(calculated_weight * product['weight'], 2)

    return tax


def create_model(request):
    """
    Creates a dictionary representing a product

    Params:
        request (LocalProxy): request containing the body of request

    Returns:
        _product (dict): product model
    """

    _json = request.json

    _name = _json['name']
    _height = float(_json['height'].replace(',', '.'))
    _length = float(_json['length'].replace(',', '.'))
    _width = float(_json['width'].replace(',', '.'))
    _weight = float(_json['weight'].replace(',', '.')) / 1000
    _price = float(_json['price'].replace(',', '.'))

    _product = {
        'name': _name,
        'height': _height,
        'length': _length,
        'width': _width,
        'weight': _weight,
        'price': _price
    }

    return _product


@app.route('/tax', methods=['POST'])
def get_tax():
    """
    Returns the impost's value for the product from request

    Params:
        payload (json): product

    Returns:
        response (dict): tax value
    """
    product = create_model(request)
    response = {'tax': str(calculate_tax(product)).replace('.', ',')}

    return response


@app.route('/track', methods=['POST'])
def add_product():
    """
    Adds product on database

    Params:
        payload (json): product

    Returns:
        _id (int): just added product id in database 
    """
    product = create_model(request)
    product['tax'] = calculate_tax(product)

    products_quantity = mongo.db.products.count()

    if products_quantity == 0:
        product['_id'] = 0
    else:
        product['_id'] = products_quantity

    query = mongo.db.products.insert_one(product)

    return {'_id': query.inserted_id}


@app.route('/track/<id>', methods=['GET'])
def product(id):
    """
    Searches for a product according to the id provided at url

    Params:
        id (str): id requested

    Returns:
        resp (json): product matching requested id
    """
    query = mongo.db.products.find_one({"_id": int(id)})
    resp = dumps(query)

    return resp


if __name__ == '__main__':
    app.run()
