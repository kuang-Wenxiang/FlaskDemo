from demo_case.user import user_api

from flask_restful import Resource

from demo_case import models, db

from commont.tools import to_dict_msg
from flask import request, g


class User(Resource):

    @staticmethod
    def get():
        user = models.User.query.get(1)
        return to_dict_msg(200, user.to_dict())


user_api.add_resource(User, '/UserInfo')
