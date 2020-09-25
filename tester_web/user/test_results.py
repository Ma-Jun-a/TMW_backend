from flask import Blueprint, request, make_response, jsonify

from tester_web.tables import db_session
from tester_web.tables.user import User, Results

results = Blueprint('results', __name__,url_prefix='/results')

@results.route('/list',methods=['get'])
def results_list(*args,**kwargs):
    user_id = request.json.get('user_id')
    api_id = request.json.get('api_id')
    status = request.json.get('status')
    try:
        if user_id is not None and api_id is None and status is None:
            content = []
            results = db_session.query(Results).filter_by(user_id=user_id).all()
            for result in results:

                data = {"id":result.id,"api_id":result.api_id,
                        "status": result.status,"request_data":result.request_dat,
                        "response_data":result.response_data,"date":result.date,
                        "response_code":result.response_code}
                content.append(data)
            return make_response(jsonify({"code":200,"msg":content}))
        elif user_id is not None and api_id is not None and status is None:
            content = []
            results = db_session.query(Results).filter_by(user_id=user_id).filter_by(api_id=api_id).all()
            for result in results:
                data = {"id": result.id, "api_id": result.api_id,
                        "status": result.status, "request_data": result.request_dat,
                        "response_data": result.response_data, "date": result.date,
                        "response_code": result.response_code}
                content.append(data)
            return make_response(jsonify({"code": 200, "msg": content}))
        elif user_id is not None and api_id is not None and status is not None:
            content = []
            results = db_session.query(Results).filter_by(user_id=user_id).filter_by(api_id=api_id).filter_by(status=status).all()
            for result in results:
                data = {"id": result.id, "api_id": result.api_id,
                        "status": result.status, "request_data": result.request_dat,
                        "response_data": result.response_data, "date": result.date,
                        "response_code": result.response_code}
                content.append(data)
            return make_response(jsonify({"code": 200, "msg": content}))
        elif user_id is not None and api_id is  None and status is not None:
            content = []
            results = db_session.query(Results).filter_by(user_id=user_id).filter_by(status=status).all()
            for result in results:
                data = {"id": result.id, "api_id": result.api_id,
                        "status": result.status, "request_data": result.request_dat,
                        "response_data": result.response_data, "date": result.date,
                        "response_code": result.response_code}
                content.append(data)
            return make_response(jsonify({"code": 200, "msg": content}))
        elif user_id is None and api_id is not None and status is not None:
            content = []
            results = db_session.query(Results).filter_by(api_id=api_id).filter_by(
                status=status).all()
            for result in results:
                data = {"id": result.id, "api_id": result.api_id,
                        "status": result.status, "request_data": result.request_dat,
                        "response_data": result.response_data, "date": result.date,
                        "response_code": result.response_code}
                content.append(data)
            return make_response(jsonify({"code": 200, "msg": content}))
        elif user_id is None and api_id is  None and status is not None:
            content = []
            results = db_session.query(Results).filter_by(
                status=status).all()
            for result in results:
                data = {"id": result.id, "api_id": result.api_id,
                        "status": result.status, "request_data": result.request_dat,
                        "response_data": result.response_data, "date": result.date,
                        "response_code": result.response_code}
                content.append(data)
            return make_response(jsonify({"code": 200, "msg": content}))
        elif user_id is None and api_id is not None and status is  None:
            content = []
            results = db_session.query(Results).filter_by(api_id=api_id).all()
            for result in results:
                data = {"id": result.id, "api_id": result.api_id,
                        "status": result.status, "request_data": result.request_dat,
                        "response_data": result.response_data, "date": result.date,
                        "response_code": result.response_code}
                content.append(data)
            return make_response(jsonify({"code": 200, "msg": content}))
    except Exception as e:
        print(e)
        return make_response(jsonify({"code": 200, "error_msg": u'查询失败'}))
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


@results.route('/delete',methods=['post'])
def results_delete(*args,**kwargs):
    results_id = request.json.get("results_id")# 有可能报错这里
    try:
        result = db_session.query(Results).filter(Results.id.in_(results_id)).all()
        db_session.delete(result)
        db_session.commit()
        return make_response(jsonify({"code":200,"msg":u'删除成功'}))
    except Exception as e:
        print('results_delete接口有可能results_id参数格式错误')
        return make_response(jsonify({"code":404,"error_msg":u'删除失败'}))



