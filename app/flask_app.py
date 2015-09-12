from flask import Flask
from config import config
from flask.ext.cors import CORS
import itsdangerous

flask_app = Flask(__name__)
flask_app.debug = config.debug()
flask_app.config.update(
    SQLALCHEMY_DATABASE_URI=config.database_connection_string(),
    CORS_HEADERS="Content-Type",
    CORS_RESOURCES={
        r"/api/*": {
            "origins": config.allowed_origins()
        }
    })

CORS(flask_app, supports_credentials=True)

flask_app.secret_key = config.secret_key()
flask_app.signer = itsdangerous.URLSafeTimedSerializer(flask_app.secret_key)
