from flask.ext.restful import Api

from app.flask_app import flask_app

api = Api(flask_app, catch_all_404s=True)
