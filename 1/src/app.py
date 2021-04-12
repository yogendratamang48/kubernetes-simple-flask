from flask import Flask, jsonify
import os
app = Flask(__name__)

country_list = [
    'Nepal',
    'India',
    'Germany',
    'Netherlands',
    'Turkey',
]

@app.route('/checkdb')
def get_credentials():
    """test function to read database
    """
    db_user = os.environ.get('DB_USER')
    db_pass = os.environ.get('DB_PASS')
    if db_user == "admin" and db_pass == "password":
        response_dict = {"message": "User and Password match"}
        return jsonify(response_dict), 200
    else: 
        response_dict = {"message": "ERROR: User and Password do not match"}
        return jsonify(response_dict), 200

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