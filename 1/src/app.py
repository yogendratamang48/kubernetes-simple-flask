from flask import Flask, jsonify
app = Flask(__name__)

country_list = [
    'Nepal',
    'India',
    'Germany',
    'Netherlands',
    'Turkey',
]

@app.route('/')
def index():
    response_dict = {
        "message": "Welcome to FlaskApp with CI with GitHub Actions"
    }
    return jsonify(response_dict)

@app.route('/notfound')
def not_found():
    response_dict = {
        "message": "Not found"
    }
    return jsonify(response_dict), 404

@app.route('/names')
def countries():
    country_dict = {
        'countries': country_list,
        'total': len(country_list)
    }
    return jsonify(country_dict)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8082)