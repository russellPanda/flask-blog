from flask import render_template, flash, redirect, url_for, Blueprint
from flask_login import login_user, logout_user, login_required, current_user




auth_blueprint=Blueprint('auth',__name__)




@auth_blueprint.route('/login',methods=['GET','POST'])
def login():
    pass



@auth_blueprint.route('/logout')
def logout():
    pass


