#coding:utf-8
from flask import Flask
import config
from exts import db

from apps.admin import bp as admin_bp
from apps.common import bp as common_bp 
from apps.front import bp as front_bp


def create_app():
	app = Flask(__name__)

	# 注册蓝图
	app.register_blueprint(admin_bp)
	app.register_blueprint(common_bp)
	app.register_blueprint(front_bp)


	# 引入配置
	app.config.from_object('config')
	db.init_app(app)
	return app



if __name__=="__main__":
	app = create_app()
	app.run(debug=True)