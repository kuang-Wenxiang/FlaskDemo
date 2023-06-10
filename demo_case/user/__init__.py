from flask import Blueprint
from flask_restful import Api

user_bp = Blueprint("User", __name__, url_prefix='/User')

user_api = Api(user_bp)

from demo_case.user import views
