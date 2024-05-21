from datetime import datetime
import requests
from flask import jsonify, Flask

request_web_app = Flask(__name__)

t_request_info_list = []
t_request_cnt = 0

@request_web_app.route('/time', methods=['GET'])
def t_get():
    global t_request_info_list
    global t_request_cnt
    t_request_cnt += 1
    resp = requests.get('http://worldtimeapi.org/api/timezone/Europe/Moscow')
    return resp.json()['datetime']

@request_web_app.route('/statistics', methods=['GET'])
def stats_get():
    global t_request_cnt
    return jsonify({'t_request_cnt': t_request_cnt})

request_web_app.run(port=7777, host='0.0.0.0')