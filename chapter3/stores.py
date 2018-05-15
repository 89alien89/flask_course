from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

stores = [
    {
        'name': 'predefined_store',
        'items': [
            {
                'name': 'predefined_item',
                'price': 1
            }
        ]
    }
]


@app.route('/')
def display_index():
    return render_template('index.html')


@app.route('/store', methods=['GET'])
def get_stores():
    return jsonify({'stores': stores})


def store_exists(name):
    s = {s['name'] for s in stores}
    return name in s


def error_response(txt):
    return jsonify({'msg': txt})


@app.route('/store', methods=['POST'])
def create_store():
    print('create store')
    request_data = request.get_json()
    if store_exists(request_data['name']):
        return error_response('store already exists')

    new_store = {
                    'name': request_data['name'],
                    'items': []
                }
    stores.append(new_store)
    return jsonify(new_store)


@app.route('/store/<string:name>')
def get_store(name):
    if not store_exists(name):
        return error_response('there is no such store')

    for s in stores:
        if s['name'] == name:
            return jsonify(s)


@app.route('/store/<string:name>/item')
def get_items(name):
    if not store_exists(name):
        return error_response('there is no such store')
    for s in stores:
        if s['name'] == name:
            return jsonify({'items': s['items']})


@app.route('/store/<string:name>/item', methods=['POST'])
def create_item(name):
    if not store_exists(name):
        return error_response('there is no such store')

    request_data = request.get_json()
    for s in stores:
        if s['name'] == name:
            obj = {'name': request_data['name'], 'price': request_data['price']}
            s['items'].append(obj)
            return jsonify(obj)

app.run(port=5000)