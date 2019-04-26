from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(10),unique=True,nullable=False)
    password = db.Column(db.String(255),nullable=False)
    is_delete = db.Column(db.Boolean,default=0)
    create_time = db.Column(db.DateTime,default=datetime.now)
    __tablename__ = 'user'

    def save(self):
        db.session.add(self)
        db.session.commit()

class Article(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(30),unique=True,nullable=False)
    content = db.Column(db.String(250),nullable=False)
    category = db.Column(db.String(30),nullable=False)
    tags = db.Column(db.String(30),nullable=False)
    create_time = db.Column(db.DateTime,default=datetime.now)
    # oprete_time = db.Column(db.DateTime,default=datetime.now, onupdate=datetime.now)
    __tablename__ = 'article'

class ArticleType(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    #栏目名称
    name = db.Column(db.String(30),unique=True,nullable=False)
    #栏目别名
    alias = db.Column(db.String(30),nullable=False)
    __tablename__ = 'art_type'







