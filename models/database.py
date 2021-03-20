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
database_file = os.getenv('CLEARDB_DATABASE_URL')
# database_file = 'mysql+pymysql://{user}:{password}@{host}/{db}?charset=utf8'.format(**{
#     'user': os.getenv('DB_USERNAME', os.environ['b8e9ff724a7a6b']),
#     'password': os.getenv('DB_PASSWORD', os.environ['886f95f0']),
#     'host': os.getenv('DB_HOST', os.environ['us-cdbr-east-03.cleardb.com']),
#     'db': os.getenv('DB_DATABASE', os.environ['heroku_9e15f4d597e722d'])
# })
# database_file = 'mysql+pymysql://{user}:{password}@{host}/todo?charset=utf8'.format(**{
#     'user': os.getenv('DB_USER','user1'),
#     'password': os.getenv('DB_PASSWORD','user1'),
#     'host': os.getenv('DB_HOST','localhost'),
# })

engine = create_engine(database_file, encoding="utf-8", echo=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    import models.models
    Base.metadata.create_all(bind=engine)
