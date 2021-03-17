# テーブルの絡む情報を定義するためのクラスを作成
from sqlalchemy import Column, Integer, String, Text, DateTime
from models.database import Base
from datetime import datetime


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    title = Column(String(30),nullable=False)
    detail = Column(String(100))
    due = Column(DateTime, nullable=False)
    user_name = Column(String(30) ,nullable=False)


    def __init__(self, title=None, detail=None, due=None, user_name=None):
        self.title = title
        self.detail = detail
        self.due = due
        self.user_name = user_name

    
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(128), unique=True)
    hashed_password = Column(String(128))

    def __init__(self, user_name=None, hashed_password='None'):
        self.user_name = user_name
        self.hashed_password = hashed_password

