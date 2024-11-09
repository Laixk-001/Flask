# -*- coding:utf-8 -*-
"""
    id = 3
    文件描述：
        部署Flask应用，主要运用多线程与多进程，提高接口的并发能力
"""

import time
import datetime
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    time.sleep(15)
    return 'Hello World!'

@app.route('/index')
def beijing():
    return 'Shanghai'

@app.route('/tell_time')
def tell_time():
    start_time_desc = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    time.sleep(5)
    end_time_desc = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return jsonify({"start_time_desc":start_time_desc, "end_time_desc":end_time_desc})

@app.route('/tell_time/<int:_id>',methods=['GET'])
def hello_index(_id):
    start_time_desc = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    time.sleep(5)
    end_time_desc = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return jsonify({"id":_id, "start_time_desc":start_time_desc, "end_time_desc":end_time_desc})

if __name__ == '__main__':
    # app.run(host='0.0.0.0',port=5000,threaded=False)

    # solution 1: 将threaded打开，该应用采用多线程部署
    app.run(host='0.0.0.0',port=5000,threaded=True)

    # solution 2: 使用gevent模块

    # solution 3: 使用gunicorn模块