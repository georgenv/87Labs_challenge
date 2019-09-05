import json
import requests

# The root url of the flask app
url = 'http://127.0.0.1:5000' 

product = {
    'name': 'Magic Mouse',
    'height': '0,75',
    'length': '1,10',
    'width': '0,60',
    'weight': '400',
    'price': '150,00'
}

def test_tax_route():
    r = requests.post(url + '/tax', json=product)
    r_json = json.loads(r.text)
    tax = r_json['tax']
    assert tax == '59,4'

def test_insert_product():
    r = requests.post(url + '/track', json=product)
    r_json = json.loads(r.text)
    print(type(r_json['_id']))
    assert isinstance(r_json['_id'], int)