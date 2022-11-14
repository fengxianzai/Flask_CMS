#coding:utf-8
from flask import Blueprint,render_template,url_for,request,session,redirect
from flask import make_response,session
from io import BytesIO
from utils.captcha import create_validate_code
from .models import Users
from .forms import LoginForm
from .decorators import login_required
bp = Blueprint("admin",__name__,url_prefix='/admin')


# 后台首页路由
@bp.route('/index')
@login_required
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
		captcha = request.form.get('captcha')
		online = request.form.get('online')
		if users:
			if user == users.username and pwd == users.password:
				if session.get('image').lower() != captcha.lower():
					return render_template('/admin/login.html',message='验证码错误',form=form)
				else:
					session['user_id'] = users.uid
					if online:
						session.permanent = True
					return redirect(url_for('admin.admin_index'))
			else:
				error = '密码错误！'
				return render_template('/admin/login.html',message=error,form=form)
		else:
			error = '没有此用户！'
			return render_template('/admin/login.html',message=error,form=form)

	else:
		return render_template('/admin/login.html',form=form)



# 调用验证码
@bp.route('/code')
def get_code():
	code_image,strs = create_validate_code()
	buf = BytesIO()
	code_image.save(buf,'JPEG',quality=70)
	buf_str = buf.getvalue()
	response = make_response(buf_str)
	response.headers['Content-Type'] = 'image/jpeg'
	# 将验证码存储在session中
	session['image'] = strs
	return response