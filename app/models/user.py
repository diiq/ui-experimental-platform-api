from sqlalchemy.ext.associationproxy import association_proxy
from app.db import db, Model
from passlib.apps import custom_app_context as pwd_context
from os import urandom
from binascii import hexlify


class User(Model, db.Model):
    __tablename__ = 'users'
    id = db.Column(
        db.Integer,
        db.Sequence('users_id_seq'),
        primary_key=True)

    # User authentication information
    email = db.Column(db.String, nullable=False, unique=True)
    password_hash = db.Column(db.String, nullable=False)
    authentication_token = db.Column(db.String, nullable=False)
    _roles = db.relationship("UserRole")
    roles = association_proxy('_roles', 'role_name')

    public_attributes = [
        'id',
        'email',
        'roles'
    ]

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        if not self.authentication_token:
            self.new_authentication_token()

    @property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, value):
        self.password_hash = pwd_context.encrypt(value)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def fulfills_role(self, role):
        return role in self.roles

    def new_authentication_token(self):
        self.authentication_token = hexlify(urandom(16))


class UserQuery(db.Query):
    def authenticated(self, email, password):
        user = self.filter_by(email=email).first()
        if user and user.verify_password(password):
            return user


User.query_class = UserQuery


class UserRole(db.Model):
    __tablename__ = 'user_roles'
    id = db.Column(db.Integer,
                   db.Sequence('user_roles_id_seq'),
                   primary_key=True)
    role_name = db.Column(db.String)
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id", ondelete="CASCADE"))

    def __init__(self, role_name):
        self.role_name = role_name
