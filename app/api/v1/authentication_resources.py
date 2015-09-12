from flask import session

from resource import Resource
from errors import ForbiddenError
from v1_api import api
from app.models import User


@api.resource("/api/v1/auth")
class AuthenticationResource(Resource):
    def post(self, email, password):
        # Get user or raise Error
        user = User.query.authenticated(email, password)
        if not user:
            raise ForbiddenError
        session["current_user"] = user.id

    def delete(self):
        del session["current_user"]

    def get(self):
        return {
            "ok": "there"
        }
