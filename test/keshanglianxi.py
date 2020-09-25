from flask import Flask, abort
from flask import Flask, abort
import settings
app.MYSQL_URL = 'python25'
def db_query():
    user_id = g.user_id
    user_name = g.user_name
    print('user_id {} user_name {}'.format(user_id,user_name))
# 先从环境变量中加载配置信息，在从配置文件中加载
def create_flask_app():
    app = Flask(__name__)
    # app.config.from_envvar('CONFIG',silent=False)
    return app

def create_app(config_name):
    app = create_flask_app()
    app.config.from_object(config_name)
    return app
app = create_app(settings.config_dict['DEV'])

# 先从环境变量中加载配置信息，在从配置文件中加载
def create_flask_app():
    app = Flask(__name__)
    # app.config.from_envvar('CONFIG',silent=False)
    return app

def create_app(config_name):
    app = create_flask_app()
    app.config.from_object(config_name)
    return app
app = create_app(settings.config_dict['DEV'])
import re
from flask import Flask, Blueprint
from flask_restful import Api, inputs, fields, marshal_with, Resource
from flask_restful.reqparse import RequestParser
from flask import make_response, current_app
from flask_restful.utils import PY3
from json import dumps

app = Flask(__name__)
user_bp = Blueprint('user_bp',__name__)
api = Api(app)
user_api = Api(user_bp)

#装饰器.py
def decorator1(f):
    def wrapper(*args,**kwargs):
        print('装饰器1运行')
        return f(*args,**kwargs)
    return wrapper
def decorator2(f):
    def wrapper(*args,**kwargs):
        print('装饰器2运行')
        return f(*args,**kwargs)
    return wrapper

class User(object):
    def __init__(self,username,mobile,user_id):
        self.username = username
        self.mobile = mobile
        self.user_id = user_id
data_files = {
    'username': fields.String,
    'mobile': fields.Integer,
    'user_id': fields.Integer,
}
@api.representation('application/json')
def output_json(data, code, headers=None):
    """Makes a Flask response with a JSON encoded body"""
    settings = current_app.config.get('RESTFUL_JSON', {})
    data = {
        'message': code,
        'data': data,
   }
    if current_app.debug:
        settings.setdefault('indent', 4)
        settings.setdefault('sort_keys', not PY3)
    dumped = dumps(data, **settings) + "\n"

    resp = make_response(dumped, code)
    resp.headers.extend(headers or {})
    return resp
#手动调用装饰器 api.representation('application/json')(output_json)

class UserResources(Resource):
    @staticmethod
    def mobile_parameter(data):
        if re.match(r'1[3-9]\d{9}$',data):
            return data
        else:
            return ValueError('mobile input error')
    @marshal_with(data_files,envelope='user_info')
    def get(self):
        #处理请求参数
        req = RequestParser()
        req.add_argument('username',type=str ,action='append' ,required=True,help='required a parameters')
        req.add_argument('mobile',type=inputs.regex('1[3-9]\d{9}') ,action='stored' ,required=True,help='required a parameters')
        req.add_argument('user_id',type=UserResources.mobile_parameter ,location='args',action='stored' ,required=True,help='required a parameters')
        # location 参数位置，get能够传递非表单操作 form args headers cookies json files
        args = req.parse_args()
        username,mobile,user_id = args.get('username'),args.get('mobile'),args.get('user_id')
        user = User(username,mobile,user_id)
        return user

class IndexResources(Resource):
    method_decorators = {
        'get': [decorator1],
        'post': [decorator2],
    }
    def get(self):
        return {'hello':'index page'}
    def post(self):
        return  {'message':'index page post'}
api.add_resource(IndexResources,'/',endpoint='index')
user_api.add_resource(UserResources,'/user',)
user_api.representation('application/json')(output_json)
app.register_blueprint(user_bp)

if __name__ == '__main__':
    print(app.url_map)
    # app.run(debug=True,host='0.0.0.0')
    app.run(debug=True)

@app.route('/error')
def index():
    abort(400)
    return '我去你'
@app.errorhandler(400)
def error_hand(e):
    return '自定义报错信息 %s'% e
# # 请求钩子
@app.route('/')
def index1():
    ret = 'index page'
    return ret
@app.before_first_request
def before_first_request():
    print('第一次请求前执行')
@app.before_request
def before_request():
    print('在所有请求前执行')
@app.after_request
def after_request(ret):
    print('当请求成功时执行')
    return ret
@app.teardown_request
def teardown_request(e):
    print('请求错误时也执行')

if __name__ == '__main__':
    app.run(debug=True, port=8989)