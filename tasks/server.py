from flask_failsafe import failsafe
from fabric.api import task


@failsafe
def server_app():
    from app.flask_app import flask_app
    return flask_app


@task(default="true")
def flask(port=5000):
    """Runs a development server."""
    server_app().run()
