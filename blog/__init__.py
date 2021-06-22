import os
import logging
from logging.handlers import SMTPHandler,RotatingFileHandler


import click


from flask import Flask,render_template,request
from flask_login import current_user
from flask_sqlalchemy import get_debug_queries
from flask_wtf.csrf import CSRFError


from blog.blueprints.admin import admin_blueprint
from blog.blueprints.auth import auth_blueprint
from blog.blueprints.blog import blog_blueprint

from blog.extensions import bootstrap,db,login_manager,csrf,editor,mail,moment,migrate
from blog.models import Admin,Post,Category,Comment,Link
from blog.setting import config

basedir=os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


def create_app(config_name=None):
    if config_name is None:
        config_name=os.getenv('FLASK_CONFIG','development')

    app=Flask('blog')
    app.config.from_object(config[config_name])

    # 注册插件




    return app




def register_extensions(app):
    """注册插件"""
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)
    editor.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    migrate.init_app(app)


def register_blueprints(app):
    """注册蓝图"""
    app.register_blueprint(admin_blueprint,url_prefix='/admin')
    app.register_blueprint(auth_blueprint,url_prefix='auth')
    app.register_blueprint(blog_blueprint)


def register_shell_context(app):
    """注册flask shell 加载内容"""
    pass



def register_logging(app):

    return app

def register_template_context(app):
    pass

def register_errors(app):
    pass


def register_commands(app):
    """注册命令 flask [cmd]"""
    pass

def register_request_handlers(app):
    pass
