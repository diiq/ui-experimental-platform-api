from flask import session

from resource import Resource
from v1_api import api
from app.models import User
from app.db import db
from errors import BadInputError


@api.resource("/api/v1/users")
class UserResource(Resource):
    def post(self, email, password):
        user = User.query.authenticated(email, password)
        if user:
            return user

        elif User.query.filter_by(email=email).first():
            raise BadInputError("You've already signed up with that email!")

        user = User(email=email, password=password)
        try:
            db.session.add(user)
            db.session.commit()
            session["current_user"] = user.id
            return user

        except:
            db.session.rollback()
            raise BadInputError("Signup Failed.")
