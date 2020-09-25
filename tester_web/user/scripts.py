from flask import Blueprint, request, make_response, jsonify
from sqlalchemy import and_
from sqlalchemy.orm import query

from tester_web.tables import db_session
from tester_web.tables.user import User, Api, Script, ApiUser, UserScript

scripts = Blueprint('scripts', __name__,url_prefix='/scripts')

@scripts.route('/list',methods=['get'])
def script_list(*args,**kwargs):
    # db_session.query()
    username = request.json.get("username")
    api = request.json.get("api")
    try:
        if username is not None and api is None:

            user = db_session.query(User).filter_by(username=username).one()
            user_apis = db_session.query(UserScript.id).filter_by(user_id=user.id).all()
            scripts = db_session.query(Script).filter(Script.api_user_id.in_(user_apis)).all()
            content = []
            for script in scripts:
                data = {"id":script.id,"description":script.description,
                        "script_content": script.script_content}
                content.append(data)
            return make_response(jsonify({"code": 200,"msg":content}))
        elif username is  None and api is not None:
            content = []
            api = db_session.query(Api).filter_by(api=api).one()
            user_apis = db_session.query(UserScript.id).filter_by(api_id=api.id).all()
            scripts = db_session.query(Script).filter(Script.api_user_id.in_(user_apis)).all()
            for script in scripts:
                data = {"id":script.id,"description":script.description,
                        "script_content": script.script_content}
                content.append(data)
            return make_response(jsonify({"code": 200, "msg": content}))

        else:
            user_api = db_session.query(UserScript.id).filter_by(user_id=api.id).filter_by(api_id=api.id).one()
            script = db_session.query(Script).filter_by(api_user_id=user_api).one()
            content = []
            data = {"id": script.id, "description": script.description,
                    "script_content": script.script_content}
            content.append(data)
            return make_response(jsonify({"code": 200, "msg": content}))
    except Exception as e:
        return  make_response(jsonify({"code": 404, "error_msg": e}))


@scripts.route('/add',methods=['post'])
def script_add(*args,**kwargs):
    # 用户自己添加脚本或者，
    username = request.json.get('username')
    api_description = request.json.get('api_description')
    try:
        user = db_session.query(User).filter_by(username=username).one()
        user_id = user.id
        api = db_session.query(Api).filter_by(api_description=api_description).one()
        api_id = api.id
        api_user = db_session.query(ApiUser).filter_by(user_id=user_id,api_id=api_id).one()
        api_user_id = api_user.id
    except Exception as e:
        return make_response(jsonify({"code": 404,"error_msg":e}))
    script_content = request.json.get('script_content')
    description = request.json.get('script_description')
    try:
        script = Script(api_user_id=api_user_id,script_content=script_content,description=description)
        db_session.add(script)
        db_session.commit()
        return make_response(jsonify({"code": 200,"msg": u'脚本添加成功'}))
    except Exception as e:
        return make_response(jsonify({"code": 404, "error_msg": e}))


@scripts.route('/adduser',methods=['post'])
def script_adduser(*args,**kwargs):
    user_id = request.json.get('user_id')
    script_id = request.json.get('script_id')
    try:
        userscript = UserScript(user_id=user_id,script_id=script_id)
        db_session.add(userscript)
        db_session.commit()
        return make_response(jsonify({"code": 200, "msg": u'添加用户成功'}))
    except Exception as e:
        return make_response(jsonify({"code": 404, "msg": e}))
    # 为某个用户添加脚本权限，都能看到，但是只有有权限的用户才能修改

@scripts.route('/delete',methods=['post'])
def script_delete(*args,**kwargs):
    user_id = request.json.get('user_id')
    script_id = request.json.get('script_id')
    try:
        script = db_session.query(UserScript).filter_by(user_id=user_id).filter_by(script_id=script_id).one()

        if script.id is not None:
            db_session.query(Script).filter_by(script_id=script_id).delete()
            db_session.commit()
            return make_response(jsonify({"code": 200, "msg": u'脚本删除成功'}))

    except Exception as e:
        return make_response(jsonify({"code": 404, "msg": e}))

@scripts.route('/upgrade',methods=['post'])
def script_upgrade(*args,**kwargs):
    user_id = request.json.get('user_id')
    script_id = request.json.get('script_id')
    script_content = request.json.get('script_content')
    description = request.json.get('script_description')
    try:
        script = db_session.query(UserScript).filter_by(user_id=user_id).filter_by(script_id=script_id).one()

        if script.id is not None:
            db_session.query(Script).filter_by(script_id=script_id).update(script_content=script_content,description=description)
            db_session.commit()
            return make_response(jsonify({"code": 200, "msg": u'脚本更新成功'}))

    except Exception as e:
        return make_response(jsonify({"code": 404, "msg": e}))

@scripts.route('/run',methods=['POST'])
def script_run(*args,**kwargs):
    pass


