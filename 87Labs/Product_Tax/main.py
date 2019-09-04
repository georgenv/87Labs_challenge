from flask import jsonify, request
from app import app, mongo
# from Product import Product


def _calculate_tax(product):
    tax = 0
    volume = product['height'] * product['width'] * product['length']
    calculated_weight = volume * 300

    if calculated_weight <= 100:
        tax = round(0.05 * product['price'], 2)
    else:
        tax = round(calculated_weight * product['weight'], 2)

    return tax


def _create_model(request):
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
def calculate_tax():
    product = _create_model(request)
    response = {'tax': str(_calculate_tax(product)).replace('.', ',')}

    return response


@app.route('/track', methods=['POST'])
def add_product():
    product = _create_model(request)
    product['tax'] = _calculate_tax(product)

    products_quantity = mongo.db.products.count()

    if products_quantity == 0:
        product['_id'] = 0
    else:
        product['_id'] = products_quantity
    
    query = mongo.db.products.insert_one(product)

    return {'_id': query.inserted_id}


if __name__ == '__main__':
    app.run()
