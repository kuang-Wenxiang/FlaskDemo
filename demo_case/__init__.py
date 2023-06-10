from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_apscheduler import APScheduler

from log.log import Logger
from config import Config

logger = Logger()
scheduler = APScheduler()
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    obj = config_map.get(config_name)
    app.config.from_object(obj)
    logger.init_app(app)
    db.init_app(app)
    scheduler.init_app(app)
    scheduler.start()

    # 用户信息
    from demo_case.user import user_bp
    app.register_blueprint(user_bp)

    return app


class DevelopmentConfig(Config):
    DEBUG = True


class ProductConfig(Config):
    DEBUG = False


config_map = {
    "develop": DevelopmentConfig,
    "product": ProductConfig
}