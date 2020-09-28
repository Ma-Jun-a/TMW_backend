#执行此方法依据模型建表
from sqlalchemy.orm import sessionmaker

from tester_web.tables.user import Model, engine


def init_db():
    Model.metadata.create_all(bind=engine)
# 先迁移模型完成后 再初始化session

# init_db()
Session = sessionmaker()
db_session = Session(bind=engine)