from flask import Blueprint, request, make_response, jsonify

from tester_web.tables import db_session
from tester_web.tables.user import User, Api, Project, UserScript, Script

api = Blueprint('api', __name__,url_prefix='/api')

@api.route('/list',methods=['get'])
def api_list(*args,**kwargs):
    project_name = request.json.get("project")
    try:
        data = {}
        project = db_session.query(Project).filter_by(project=project_name).one()
        apis = db_session.query(Api).filter_by(project_id=project.id).all()
        for api in apis:
            data = {
                "id":api.id,
                "project_id":api.project_id,
                "module_sub":api.module_sub,
                "api_description":api.api_description
            }
            # data = {"test": '我是test'}
        return make_response(jsonify({"code":200,"msg":data}))
    except Exception as e:
        return  make_response(jsonify({"code": 404,"error_msg": e}))


@api.route("/scriptslist",methods=["post"])
def api_scriptslist(*args,**kwargs):
    api_id = request.json.get("api_id")
    try:
        user_apis = db_session.query(UserScript.id).filter_by(api_id=api_id).all()
        scripts = db_session.query(Script).filter(Script.api_user_id.in_(user_apis)).all()
        data = {}
        for script in scripts:
            data = {"id": script.id, "description": script.description,
                    "script_content": script.script_content}
        return make_response(jsonify({"code": 200, "msg": data}))
    except Exception as e:
        return  make_response(jsonify({"code": 404,"error_msg":e}))


@api.route('/add',methods=['post'])
def api_add(*args,**kwargs):

    project_name = request.json.get("project_name")
    module_sub = request.json.get("module_sub")
    api_description = request.json.get("api_description")  # 接口描述
    try:
        project = db_session.query(Project).filter_by(project=project_name).one()
        api = Api(project_id=project.id,module_sub=module_sub,api_description=api_description)
        db_session.add(api)
        db_session.commit()
        return make_response(jsonify({"code":200,"msg": u'新增接口成功'}))
    except Exception as e:
        return make_response(jsonify({"code":404,"error_msg": u'新增接口失败'}))


@api.route('/delete',methods=['post'])
def api_delete(*args,**kwargs):

    api_id = request.json.get('api_id')  # 接口描述
    try:
        api = db_session.query(Api).filter_by(id=api_id).one()
        db_session.delete(api)
        db_session.commit()
        return make_response(jsonify({"code":200,"msg": u'删除接口成功'}))
    except Exception as e:
        return make_response(jsonify({"code":404,"error_msg": u'新增接口失败'}))


@api.route('/upgrade',methods=['post'])
def api_upgrade(*args,**kwargs):
    api_id = request.json.get('api_id')  # 接口描述
    # project_name = request.json.get("project_name")
    module_sub = request.json.get("module_sub")
    api_description = request.json.get("api_description")
    try:
        db_session.query(Api).filter_by(id=api_id).upgrade(module_sub=module_sub,
                                                                 api_description=api_description)

        db_session.commit()

        return make_response(jsonify({"code":200,"msg": u'修改接口成功'}))
    except Exception as e:
        return make_response(jsonify({"code":404,"error_msg": u'新增接口失败'}))

