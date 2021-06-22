from flask import render_template,flash,redirect,url_for,request,current_app,Blueprint,abort,make_response
from flask_login import current_user



blog_blueprint=Blueprint('blog',__name__)




@blog_blueprint.route('/')
def index():
    pass


@blog_blueprint.route('/about')
def about():
    pass


@blog_blueprint.route('/category/<int:category_id>')
def show_category():
    pass


@blog_blueprint.route('/post/<int:post_id>',methods=['GET','POST'])
def show_post():
    pass


@blog_blueprint.route('/reply/comment/<int:comment_id>')
def reply_comment():
    pass



@blog_blueprint.route('/change-theme/<theme_name>')
def change_theme():
    pass