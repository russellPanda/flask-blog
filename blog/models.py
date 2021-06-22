from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from blog.extensions import db


class Admin(db.Model, UserMixin):
    """ 平台用户"""

    id = db.Column(db.Integer, primary_key=True)  # 主键
    username = db.Column(db.String(20))
    password = db.Column(db.String(20))
    name = db.Column(db.String(20))
    blog_title = db.Column(db.String(60))
    blog_sub_title = db.Column(db.String(100))
    about = db.Column(db.Text)


class Category(db.Model):
    """ 文章分类"""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)


class Post(db.Model):
    """ 文章"""

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    can_comment = db.Column(db.Boolean, default=True)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))


class Comment(db.Model):
    """ 评论"""
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(30))
    email = db.Column(db.String(254))
    site = db.Column(db.String(255))
    body = db.Column(db.Text)
    from_admin = db.Column(db.Boolean, default=False)
    reviewed = db.Column(db.Boolean, default=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)

    replied_id = db.Column(db.Integer, db.ForeignKey('comment.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))


class Link(db.Model):
    """ 链接"""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    url = db.Column(db.String(255))
