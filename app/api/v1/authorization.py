from flask import session, request
from app.models import User


def current_user():
    if "current_user" in session:
        return User.query.get(session["current_user"])
    else:
        token = request.args.get("auth")
        if not token:
            return

        user = User.query.filter_by(token=token).first()
        if not user:
            return

        return user


def fulfills_role(role):
    user = current_user()
    if user:
        return user.fulfills_role(role)
    return False
