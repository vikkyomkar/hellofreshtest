# Importing required python modules
import os
from flask import Flask, jsonify,abort, make_response, request, Response, render_template
NOT_FOUND = 'Not found'
BAD_REQUEST = 'Bad request'


app = Flask(__name__)

#####  Temp datastorage #####
configs = [
    {
        'name': 'test1',
        'data' : { 'age': 10 }
    },
        {
        'name': 'test2',
        'data' : {'age': 15}
    },
]
################################
def _get_config(name):
        return [config for config in configs if config['name'] == name]


def _record_exists(name):
        return [config for config in configs if config['name'] == name]


@app.errorhandler(404)
def not_found(error):
        return make_response(jsonify({'error': NOT_FOUND}), 404)


@app.errorhandler(400)
def bad_request(error):
        return make_response(jsonify({'error': BAD_REQUEST}), 400)


@app.route('/configs', methods=['GET'])
def get_configs():
        return jsonify({'configs': configs}), 200


@app.route('/configs/<string:name>', methods=['GET'])
def get_config(name):
        config = _get_config(name)
        if not config:
                abort(404)
        return jsonify({'configs': config}), 200

@app.route('/configs', methods=['POST'])
def create_config():
        if not request.json or 'name' not in request.json:
                abort(400)
        name = request.json.get('name')
        if _record_exists(name):
                abort(400)
        age = request.json.get('data')['age']
        if type(age) is not int:
                abort(400)
        configs.append(request.json)
        return jsonify({'config': request.json}) , 201

@app.route('/configs/<string:name>', methods=['PUT'])
def update_config(name):
        config = _get_config(name)
        if len(config) == 0:
                abort(404)
        if not request.json:
                abort(400)
        name = request.json.get('name', config[0]['name'])
        age = request.json.get('data')['age']
        if type(age) is not int:
                abort(400)
        config[0]['name'] = name
        config[0]['data']['age'] = age
        return jsonify({'config': config[0]}), 200

@app.route('/search', methods=['GET'])
def get_search():
        if not request.args['name'] or not request.args['data.age']:
                abort(400)
        config = _get_config(request.args['name'])
        if len(config) == 0:
                abort(404)
        if int(config[0]['data']['age']) != int(request.args['data.age']):
                abort(404)
        return jsonify({'config': config}), 200

@app.route('/configs/<string:name>', methods=['DELETE'])
def delete_config(name):
        config = _get_config(name)
        if len(config) == 0:
                abort(404)
        configs.remove(config[0])
        return jsonify({}), 204

if __name__ == '__main__':
        try:
                if  os.environ['SERVE_PORT']:
                        app.run(debug=True, host='0.0.0.0', port=int(os.environ['SERVE_PORT']))
        except Exception as e:
                print "ERROR: SERVE_PORT not defined as env variable"
