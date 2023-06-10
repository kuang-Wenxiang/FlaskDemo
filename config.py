import os


class Config(object):
    MYSQL_DIALECT = 'mysql'
    MYSQL_DRIVER = 'pymysql'
    MYSQL_CHARSET = 'utf8mb4'
    SECRET_KEY = os.urandom(16)
    USER = 'root'
    PWD = '123456'
    DB_NAME = 'flask_demo_SQL'
    HOST = '127.0.0.1'
    PORT = 3306
    JSON_AS_ASCII = False
    SQLALCHEMY_DATABASE_URI = f"{MYSQL_DIALECT}+{MYSQL_DRIVER}://{USER}:{PWD}@{HOST}:{PORT}/{DB_NAME}?charset={MYSQL_CHARSET}"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    RESTFUL_JSON = dict(ensure_ascii=False)
    # 定时器配置
    SCHEDULER_API_ENABLED = True
