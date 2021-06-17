from flask import Flask, jsonify
import os
import socket
from logging.config import dictConfig
import requests

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)

country_list = [
    'Nepal',
    'India',
    'Germany',
    'Netherlands',
    'Turkey',
]

hostname = socket.gethostname()

IS_HEALTHY = True
@app.route('/checkdb')
def get_credentials():
    """test function to read database
    """
    db_user = os.environ.get('DB_USER')
    db_pass = os.environ.get('DB_PASS')
    if db_user == "admin" and db_pass == "password":
        response_dict = {"message": "User and Password match"}
        app.logger.info("password checks")
        return jsonify(response_dict), 200
    else: 
        response_dict = {"message": "ERROR: User and Password do not match"}
        return jsonify(response_dict), 200

@app.route('/')
def index():
    response_dict = {
        "message": "Welcome to FlaskApp with CI with GitHub Actions"
    }
    app.logger.info("Index Page")
    return jsonify(response_dict)

@app.route("/info")
def message():
    """returns info
    """
    message = os.environ.get("APP_MESSAGE", "No Message")
    host_name = os.environ.get("HOSTNAME")
    response_dict = {
        "message": f"{message}, host: {host_name}"
    }
    return jsonify(response_dict)


@app.route("/ping")
def ping():
    response_dict = {
        "message": f"Ping from {socket.gethostbyname(hostname)}"
    }
    return jsonify(response_dict)

@app.route("/pong")
def pong():
    response_dict = {
        "message": f"Pong from {socket.gethostbyname(hostname)}"
    }
    return jsonify(response_dict)


@app.route("/call-friend")
def call_friend():
    """calls another service and returns the message
    """
    service_name = os.environ.get("FRIEND_SERVICE_NAME")
    resp = requests.get(service_name)
    try:
        jdata = resp.json()
        new_data = {}
        new_data["message_from_friend"] = jdata['message']
        new_data["friend_service"] = service_name
        return jsonify(new_data)
    except Exception as e:
        app.logger.error(f"{str(e)}")
        return "Fail", 503



@app.route("/healthz")
def healthcheck():
    """checks health
    """
    
    if IS_HEALTHY:
        app.logger.info("Health Checks: Healthy")
        return "OK", 200
    else:
        app.logger.info("Health Checks: Not-Healthy")
        return "Not Healthy", 503


@app.route("/fail-service")
def fail_service():
    """
    """
    app.logger.info("Health Checks")
    global IS_HEALTHY
    IS_HEALTHY = False
    return "Pod Will Fail", 200


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
