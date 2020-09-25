from flask import Blueprint, request, make_response, jsonify

from tester_web.tables import db_session
from tester_web.tables.user import User, Project, ProjectUser

project = Blueprint('project', __name__,url_prefix='/project')

@project.route('/list',methods=['get'])
def script_list(*args,**kwargs):
    project_name = request.values.get("project")
    projects = db_session.query(Project).filter_by(project=project_name).one()

    status = request.values.get("status")
    # 1. 传入项目id后能够看到所有的脚本，添加所属人参数等过滤条件
    # 每个用户只能看到自己有权限的脚本
    pass
    # ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')
    # # users.insert().values(name='jack', fullname='Jack Jones')
    # result = db_session.query(User).filter_by(username="majun").first()
    # ed_user.nickname = 'eddie'
    # session.query(User).filter(User.name.in_(['ed', 'fakeuser'])).all()
    # session.query(User.name, User.fullname):
    # session.query(User.name.label('name_label')).all():
    # user_alias = aliased(User, name='user_alias')
    # session.query(User).order_by(User.id)[1:3]
    # query.filter(User.name.isnot(None))
    # query.filter(~User.name.in_(['ed', 'wendy', 'jack']))
    # query.filter(User.name.is_(None))
    # query.filter(and_(User.name == 'ed', User.fullname == 'Ed Jones'))
    # query.filter(or_(User.name == 'ed', User.name == 'wendy'))
    # query.filter(User.name.match('wendy'))
    # query = session.query(User.id).filter(User.name == 'ed'). \
    #     ...order_by(User.id)
    # query.scalar()
    #
    # https: // docs.sqlalchemy.org / en / 13 / orm / relationship_api.html  # sqlalchemy.orm.relationship

@project.route('/add',methods=['post'])
def project_add(*args,**kwargs):
    # 用户自己添加脚本或者，
    # 前端校验必输项
    project = request.json.get("project_name")
    version = request.json.get("project_version")
    try:
        pro = Project(project=project,version=version)
        db_session.add(pro)
        return make_response(jsonify({'code': 200, 'msg': u'添加项目成功!'}))
    except Exception as e:
        print(e)
        return make_response(jsonify({'code': 401, 'msg': u'添加项目失败!'}))

@project.route('/setProjectStatus', methods=['POST'])
def setProjectStatus():
    pass
  # user_id = session.get('user_id')
  # id = request.json.get("id")
  # status = request.json.get("status")
  # data = {'status': status}
  # row_data = Project.query.filter(db.and_(Project.id == id))
  # if row_data.first():
  #   row_data.update(data)
  #   db.session.commit()
  #   return make_response(jsonify({'code': 0, 'msg': 'sucess', 'content': []}))
  # else:
  #   return make_response(jsonify({'code': 10001, 'msg': 'no such Project', 'content': []}))

@project.route('/update',methods=['post'])
def project_update(*args,**kwargs):
    # 判断是否还有挂接的接口
    project_id = request.json.get("project_id")
    project = request.json.get("project_name")

    version = request.json.get("project_version")
    try:

        db_session.query(Project).filter_by(id=project_id).update(project=project,version=version)
        db_session.commit()

        return make_response(jsonify({'code': 200, 'msg': u'删除项目成功!'}))
    except Exception:
        return make_response(jsonify({'code': 401, 'error_msg': u'删除项目失败!'}))

@project.route('/delete',methods=['post'])
def project_del(*args,**kwargs):
    # 判断是否还有挂接的接口
    project = request.json.get("project_name")
    version = request.json.get("project_version")
    try:
        pro = Project(project=project, version=version)
        db_session.delete(pro)
        db_session.commit()
        return make_response(jsonify({'code': 200, 'msg': u'删除项目成功!'}))
    except Exception:
        return make_response(jsonify({'code': 401, 'error_msg': u'删除项目失败!'}))


@project.route('/adduser',methods=['post'])
def project_adduser(*args,**kwargs):
    project_id = request.json.get("project_id")
    user_id = request.json.get("user_id")
    try:
        pro_user = ProjectUser(project_id=project_id,user_id=user_id)
        db_session.add(pro_user)
        db_session.commit()
        return make_response(jsonify({'code': 200, 'msg': u'添加项目用户成功!'}))
    except Exception as e:
        return make_response(jsonify({'code': 401, 'error_msg': u'添加项目用户失败!'}))


@project.route('/deluser', methods=['post'])
def project_deluser(*args, **kwargs):
    project_id = request.json.get("project_id")
    user_id = request.json.get("user_id")
    try:
        pro_user = ProjectUser(project_id=project_id, user_id=user_id)
        db_session.add(pro_user)
        db_session.commit()
        return make_response(jsonify({'code': 200, 'msg': u'删除项目用户成功!'}))
    except Exception as e:
        return make_response(jsonify({'code': 401, 'error_msg': u'删除项目用户失败!'}))


