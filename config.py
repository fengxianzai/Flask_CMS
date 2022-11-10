#encoding:utf-8                              #设定编码
import os
USERNAME='root'                              #登录账号
PASSWORD='123456'                            #登录密码
HOST='127.0.0.1'                             #主机地址
PORT='3306'                                  #端口号
DATABASE='vowcms'                             #使用的数据库

DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=USERNAME,password=PASSWORD, host=HOST,port=PORT, db=DATABASE)

# 创建数据库连接示例子
SQLALCHEMY_DATABASE_URI = DB_URI

# 动态追踪修改设置，如未设置只会提示告警
SQLALCHEMY_TRACK_MODIFICATIONS = False

# 查询时会显示原始的SQL语句
SQLALCHEMY_ECHO = True

#开启CSRF
CSRF_ENABLE = True

#生成密钥
SECRET_KEY = 'codevow'
