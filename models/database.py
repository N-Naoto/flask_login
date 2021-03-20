# DBとの直接的な接続の情報を格納する
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

# sqlite3バージョン
# databese_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'todo.db') 
# engine = create_engine('sqlite:///' + databese_file, convert_unicode=True)
# db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
# Base = declarative_base()
# Base.query = db_session.query_property()

# mysqlバージョン
database_file = 'mysql+pymysql://{user}:{password}@{host}/{db}?charset=utf8'.format(**{
    'user': os.getenv('DB_USERNAME', os.environ['b7c0d0a337a95a']),
    'password': os.getenv('DB_PASSWORD', os.environ['2277403a']),
    'host': os.getenv('DB_HOST', os.environ['us-cdbr-east-03.cleardb.com']),
    'db': os.getenv('DB_DATABASE', os.environ['heroku_e7ee857d4c8a436'])
})
# database_file = 'mysql+pymysql://{user}:{password}@{host}/todo?charset=utf8'.format(**{
#     'user': os.getenv('DB_USER', os.environ['user1']),
#     'password': os.getenv('DB_PASSWORD', os.environ['user1']),
#     'host': os.getenv('DB_HOST', os.environ['localhost']),
# })
engine = create_engine(database_file, encoding="utf-8", echo=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    import models.models
    Base.metadata.create_all(bind=engine)
