from flask import render_template, flash, redirect, url_for, Blueprint
from flask_login import login_user, logout_user, login_required, current_user




admin_blueprint=Blueprint('auth',__name__)




