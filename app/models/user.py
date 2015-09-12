from app.db import db
from passlib.apps import custom_app_context as pwd_context


class User(db.Model):
    id = db.Column(
        db.Integer,
        db.Sequence('users_id_seq'),
        primary_key=True)

    # User authentication information
    email = db.Column(db.String, nullable=False, unique=True)
    password_hash = db.Column(db.String, nullable=False)
    reset_password_token = db.Column(db.String)

    @property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, value):
        self.password_hash = pwd_context.encrypt(value)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)


class UserQuery(db.Query):
    def authenticated(self, email, password):
        user = self.filter_by(email=email).first()
        if user and user.verify_password(password):
            return user


User.query_class = UserQuery
