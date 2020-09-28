import os
import time
from datetime import datetime

from sqlalchemy import create_engine, Column, Integer, DateTime, String, Text, SMALLINT, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session, relationship
os.environ["NLS_LANG"] = "GERMAN_GERMANY.UTF8"
engine = create_engine("oracle://ManagerTester:123456@192.168.1.75:1521/orcl?encoding=utf8",encoding='utf-8')
Model = declarative_base(name='Model')


class User(Model):
    __tablename__ = 'User'
    id = Column(Integer,primary_key=True,nullable=True)
    name = Column('name',String(50),nullable=False)
    password = Column('password',String(50), nullable=False)
    email =  Column('email',String(20),nullable=True)
    scripts = relationship("Script",back_populates="user")

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
    user_id = Column("user_id",ForeignKey('User.id'))
    user = relationship("User", back_populates="scripts")
    # apiuser = relationship("apiuser", back_populates="ApiUser",cascade_backrefs=False)
    # 脚本描述
    description = Column("description",Text())
    # 最终执行时间
    date = Column("date", Text())
    # 脚本信息正文
    script_content = Column("script_content", Text(), nullable=False)
    parameters = Column("parameters",Text(),nullable=False)# 可以传参的几个参数key名称
    results = relationship("Results", back_populates="script")



    def __iter__(self,description,script_content,api_user_id,parameters):
        self.date = time.time()
        self.description = description
        self.api_user_id = api_user_id
        self.parameters = parameters
        self.script_content = script_content


class UserScript(Model):
    __tablename__ = "UserScript"
    id = Column(Integer, primary_key=True, nullable=False)
    script_id = Column("script_id", Integer,nullable=False)
    user_id = Column("user_id", Integer,nullable=False)
    # script_id = Column("script_id", ForeignKey('Script.id'))
    # script = relationship("script", back_populates="UserScript")
    # user_id = Column("user_id", ForeignKey('User.id'))
    # user = relationship("user", back_populates="scripts")

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
    project_code = Column("project_code",Integer,nullable=False)
    version = Column("version",String(50))
    apis = relationship("Api",back_populates="project")
    # user_projects = relationship("user_projects", back_populates="projects")

    def __init__(self,project,version):
        self.id = time.time()
        self.project = project
        self.version = version

        # self.module_ = module

class ProjectUser(Model):
    __tablename__ = "ProjectUser"
    id = Column(Integer, primary_key=True, nullable=True)
    user_id = Column("user_id",Integer,nullable=False)
    project_id = Column("project_id",Integer, nullable=False)
    # user_id = Column("user_id", ForeignKey('User.id'))
    # user = relationship("user", back_populates="users_project")
    # project_id = Column("project_id", ForeignKey('Project.id'))
    # project = relationship("project", back_populates="users_project")

    def __init__(self,project_id,user_id):
        self.id = time.time()
        self.project_id = project_id
        self.user_id = user_id


class Api(Model):
    __tablename__ = 'Api'
    id = Column(Integer, primary_key=True, nullable=True)

    date = Column("date",String(20))
    api_description = Column("api_description",Text())# 接口描述
    module_sub = Column("module_sub",Text())
    api_document = Column("api_document",Text())
    project_id = Column("project_id",ForeignKey('Project.id'))# 所属项目
    project = relationship("Project", back_populates="apis")

    def __iter__(self,api_description,project_id,module_sub,api_document):

        self.project_id = project_id
        self.api_description = api_description
        self.api_document = api_document
        self.module_sub = module_sub
        self.date = time.time()

class ApiUser(Model):
    __tablename__ = "ApiUser"
    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column("user_id",Integer,nullable=False)
    api_id = Column("api_id", Integer, nullable=False)
    # user_id = Column("user_id", ForeignKey('User.id'))
    # user = relationship("user", back_populates="User")
    # api_id = Column("api_id", ForeignKey('Api.id'))
    # api = relationship("api", back_populates="Api")
    def __init__(self,user_id,api_id):
        self.user_id = user_id
        self.api_id = api_id


class Results(Model):
    # class STATUS:
    #     SUCCESS = 0  # 成功
    #     FAILE = 1  # 失败
    __tablename__ = 'Results'
    id = Column(Integer, primary_key=True, nullable=True)
    script_id = Column("script_id",ForeignKey("Script.id"))
    script = relationship("Script",back_populates="results")
    # user_id = Column("user_id",ForeignKey("User.id"))
    # user = relationship("user",back_populates="User" )
    # api_id = Column("api_id", ForeignKey("Api.id"))
    # api = relationship("Api", back_populates="results")
    status = Column('status',Integer)
    request_data = Column("request_data", Text())
    response_data = Column("response_data", Text())
    # assert_data = Column('assert_data',Text())
    response_code = Column("response_code",String(10))
    date = Column("date", Text())# 收到测试结果的时间
    def __init__(self,script_id,response_data,request_data,status,response_code):
        self.date = time.time()
        # self.user_id = user_id
        self.script_id = script_id
        # self.api_id = api_id
        self.response_data = response_data
        self.request_data = request_data
        self.response_code = response_code
        self.status = status





