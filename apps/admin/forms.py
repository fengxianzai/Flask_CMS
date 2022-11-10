#coding:utf-8
#引入From基类
from flask_wtf import FlaskForm

from wtforms import StringField,BooleanField,SubmitField,PasswordField
from wtforms.validators import DataRequired,Length,Email

class LoginForm(FlaskForm):
	username = StringField(
			label='用户名',
			validators=[
				DataRequired(message = '用户名为必填项'),
				Length(2,10,message = '用户名长度为介于3~10')
			],
			render_kw={'placeholder':'用户名'}
		)
	password = PasswordField(
			label = '密码',
			validators=[
				DataRequired(message = '密码为必填项'),
				Length(3,10,message = '用户名长度为介于3~10')
			],
			render_kw={'placeholder':'密码'}
		)
	submit = SubmitField('登录',render_kw={'class':'btn btn-success radius size-L'})
	reset = SubmitField('取消',render_kw={'class':'btn btn-default radius size-L'})