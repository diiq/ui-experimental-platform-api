from flask import session

from resource import Resource, requires_role
from errors import ForbiddenError
from v1_api import api
from app.models import User
import authorization


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

    def get(self, role):
        return {
            'role': role,
            'authorized': authorization.fulfills_role(role)
        }


@api.resource("/api/v1/auth/me")
class MeResource(Resource):
    @requires_role("user")
    def get(self):
        return self.current_user()
