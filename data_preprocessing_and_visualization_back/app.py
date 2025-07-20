from re import escape
from flask import Flask, request, jsonify
import json
from dealfunction.dealpath import *

#跨域
from flask_cors import CORS,cross_origin


app = Flask(__name__)

#跨域
CORS(app)

@app.route('/', methods=['get'])
def hello_world():
    return 'hello'


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)


@app.route('/testpost', methods=['post'])
def first_post():
    try:
        # my_json = request.get_json()
        my_json = request.get_data()
        print(my_json)
        # return jsonify(name=my_json['name'],age=my_json['age']+10)
        return my_json
    except Exception as e:
        print(e)
        return jsonify(msg='请查看是否正确请求参数')
    # fname=request.form.get('name')
    # return fname


@app.route('/postdata', methods=['post'])
def data_post():
    try:
        my_json = request.get_json()
        # my_json = request.get_data()
        path = my_json['path']
        print(dealcsv(path))
        # return jsonify(name=my_json['name'],age=my_json['age']+10)
        return jsonify(dealcsv(path))
    except Exception as e:
        print(e)
        return jsonify(msg='请查看是否正确请求参数')


@app.route('/getfilelist', methods=['get'])
def getlist():
    with open('dealfunction/list.json', 'r')as f:
        # json转换
        # a=json.load(f)
        # # print(a)
        # print(json.dumps(a, ensure_ascii=False))
        # return json.dumps(a, ensure_ascii=False)
        return f.read()


if __name__ == '__main__':
    app.run()
