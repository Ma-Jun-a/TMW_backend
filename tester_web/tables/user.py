import time
from datetime import datetime

from sqlalchemy import create_engine, Column, Integer, DateTime, String, Text, SMALLINT, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session, relationship

engine = create_engine("oracle://ManagerTester:123456@192.168.1.75:1521/orcl",encoding='utf-8',)
Model = declarative_base(name='Model')


class User(Model):
    __tablename__ = 'User'
    id = Column(Integer,primary_key=True,nullable=True)
    name = Column('name',String(50),nullable=False)
    password = Column('password',String(50), nullable=False)
    email =  Column('email',String(20),nullable=True)


    def __init__(self,name,password,email):
        self.id = time.time()
        self.name = name
        self.password = password
        self.email = email

class Script(Model):
    __tablename__ = 'Script'
    # administrator = relationship("MisAdministrator", uselist=False)
    id = Column(Integer, primary_key=True, nullable=False)
    # 与user的外键关联
    api_user_id = Column("api_user_id",ForeignKey('ApiUser.id'))
    apiuser = relationship("apiuser", back_populates="ApiUser")
    # apiuser = relationship("apiuser", back_populates="ApiUser",cascade_backrefs=False)
    # 脚本描述
    description = Column("description",Text())
    # 最终执行时间
    date = Column("date", Text())
    # 脚本信息正文
    script_content = Column("script_content", Text(), nullable=False)
    parameters = Column("parameters",Text(),nullable=False)# 可以传参的几个参数key名称


    def __iter__(self,description,script_content,api_user_id,parameters):
        self.date = time.time()
        self.description = description
        self.api_user_id = api_user_id
        self.parameters = parameters
        self.script_content = script_content

class UserScript(Model):
    __tablename__ = "UserScript"
    id = Column(Integer, primary_key=True, nullable=False)
    script_id = Column("script_id", ForeignKey('Script.id'))
    script = relationship("script", back_populates="UserScript")
    user_id = Column("user_id", ForeignKey('User.id'))
    user = relationship("user", back_populates="UserScript")

    def __init__(self,script_id,user_id,):
        self.script_id = script_id
        self.user_id = user_id

class Project(Model):
    class STATUS:
        SUCCESS = 0  # 停用
        FAILE = 1  # 启用

    __tablename__ = "Project"
    id = Column(Integer, primary_key=True, nullable=False)
    project = Column("project",String(50),nullable=False)
    # module_ = Column("module",String(50))
    version = Column("version",String(50))
    # status = Column("status",STATUS)
    def __init__(self,project,version):
        self.project = project
        self.version = version
        # self.module_ = module

class ProjectUser(Model):
    __tablename__ = "ProjectUser"
    id = Column(Integer, primary_key=True, nullable=True)

    user_id = Column("user_id", ForeignKey('User.id'))
    user = relationship("user", back_populates="User")
    project_id = Column("project_id", ForeignKey('Project.id'))
    project = relationship("project", back_populates="Project")

    def __init__(self,project_id,user_id):
        self.project_id = project_id
        self.user_id = user_id


class Api(Model):
    __tablename__ = 'Api'
    id = Column(Integer, primary_key=True, nullable=True)

    date = Column("date",String(20))
    api_description = Column("api_description",Text())# 接口描述
    module_sub = Column("module_sub",Text())
    project_id = Column("project_id",ForeignKey('Project.id'))# 所属项目
    project = relationship("project", back_populates="Project")
    def __iter__(self,api_description,project_id):

        self.project_id = project_id
        self.api_description = api_description
        self.date = time.time()

class ApiUser(Model):
    __tablename__ = "ApiUser"
    id = Column(Integer, primary_key=True, nullable=False)
    #
    user_id = Column("user_id", ForeignKey('User.id'))
    user = relationship("user", back_populates="User")
    api_id = Column("api_id", ForeignKey('Api.id'))
    api = relationship("api", back_populates="Api")
    def __init__(self,user_id,api_id):
        self.user_id = user_id
        self.api_id = api_id


class Results(Model):
    # class STATUS:
    #     SUCCESS = 0  # 成功
    #     FAILE = 1  # 失败
    __tablename__ = 'test_results_detail'
    id = Column(Integer, primary_key=True, nullable=True)
    script_id = Column("script_id",ForeignKey("Script.id"))
    script = relationship("script",back_populates="Script")
    user_id = Column("user_id",ForeignKey("User.id"))
    user = relationship("user",back_populates="User" )
    api_id = Column("api_id", ForeignKey("Api.id"))
    api = relationship("api", back_populates="Api")
    status = Column('status',Integer)
    request_data = Column("request_data", Text())
    response_data = Column("response_data", Text())
    # assert_data = Column('assert_data',Text())
    response_code = Column("response_code",String(10))
    date = Column("date", Text())# 收到测试结果的时间
    def __init__(self,api_id,script_id,user_id,response_data,request_data,status,response_code):
        self.date = time.time()
        self.user_id = user_id
        self.script_id = script_id
        self.api_id = api_id
        self.response_data = response_data
        self.request_data = request_data
        self.response_code = response_code
        self.status = status





