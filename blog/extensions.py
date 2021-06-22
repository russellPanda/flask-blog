# -*- coding: utf-8 -*-

# flask插件


from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from flask_login import LoginManager
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_migrate import Migrate



bootstrap=Bootstrap()
db=SQLAlchemy()
login_manager=LoginManager()
csrf=CSRFProtect()
editor=CKEditor
mail=Mail()
moment=Moment()
migrate=Migrate()



