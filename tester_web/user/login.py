from flask import Blueprint, request, render_template, redirect, make_response, jsonify
from tester_web.tables import db_session
from tester_web.tables.user import User

auth = Blueprint('login', __name__,url_prefix='/login')


@auth.route('/',methods=['POST','GET'])
def login():
    username = request.json.get("username")
    password = request.json.get("password")
    print(username)
    user_id = db_session.query(User).filter_by(username=username)
    if user_id is None:
        return make_response(jsonify({'code': 401, 'error_msg': u'用户不存在!'}))
    passwd = db_session.query(User.password).filter_by(id=user_id)
    if password == passwd:
        return make_response(jsonify({'code': 200, 'msg': u'登陆成功!'}))
    else:
        return make_response(jsonify({'code': 200, 'msg': u'密码错误!'}))



