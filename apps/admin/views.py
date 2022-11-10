#coding:utf-8
from flask import Blueprint,render_template,url_for,request,session,redirect
from .models import Users
from .forms import LoginForm
bp = Blueprint("admin",__name__,url_prefix='/admin')


# 后台首页路由
@bp.route('/index')
def admin_index():
	return render_template('admin/index.html')


# 登录路由
@bp.route('/login',methods=['GET','POST'])
def login():
	error = None
	form = LoginForm(request.form)
	print(url_for('static',filename='h-ui/css/H-ui.min.css'))
	if form.validate_on_submit():
		user = request.form.get('username')
		pwd = request.form.get('password')
		users = Users.query.filter_by(username=user).first()
		if users:
			if user == users.username and pwd == users.password:
				session['user_id'] = users.uid
				return redirect(url_for('admin.admin_index'))
			else:
				error = '用户名或密码错误！'
				return render_template('/admin/login.html',message=error,form=form)
		else:
			error = '没有此用户！'
			return render_template('/admin/login.html',message=error,form=form)
	else:
		return render_template('/admin/login.html',form=form)



