import os

from demo_case import db

from datetime import datetime

from dotenv import load_dotenv, find_dotenv

from werkzeug.security import generate_password_hash, check_password_hash

# from commont.utils.status import status

load_dotenv(find_dotenv())

min_len = int(os.getenv("min_len"))
middle_len = int(os.getenv("middle_len"))
comment_len = int(os.getenv("comment_len"))
long_len = int(os.getenv("long_len"))


class BaseModel:
    # 创建时间
    create_time = db.Column(db.DateTime, default=datetime.now)
    # 修改时间
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    # 是否已经删除，默认false未删除
    is_delete = db.Column(db.Boolean, default=False)


class User(db.Model, BaseModel):
    # 自增ID
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 用户名称
    user_name = db.Column(db.String(middle_len), nullable=True)
    # 登录密码
    user_password = db.Column(db.String(comment_len), nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "user_name": self.user_name
        }

    @property
    def password(self):
        return self.user_password

    @password.setter
    def password(self, t_pwd):
        self.user_password = generate_password_hash(t_pwd)

    def check_password(self, t_pwd):
        return check_password_hash(self.user_password, t_pwd)
