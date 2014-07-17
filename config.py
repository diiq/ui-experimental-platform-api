import os


class Config(object):
    # TODO memoize these?

    def _bool(self, str):
        if str:
            return str.upper() == "TRUE"

    def project_root(self):
        return os.path.abspath(os.path.dirname(__file__))

    def root_url(self):
        return os.environ.get('ROOT_URL')

    def frontend_url(self):
        return os.environ.get('FRONTEND_URL')

    def database_connection_string(self):
        return os.environ.get('DATABASE_URL')

    def database_name(self):
        return os.environ.get('RDS_DB_NAME') or os.environ.get('DATABASE_NAME')

    def debug(self):
        return self._bool(os.environ.get('FLASK_DEBUG'))

    def alembic_ini(self):
        return "%s/alembic/alembic.ini" % self.project_root()

    def allowed_origins(self):
        return map(lambda x: x.strip(),
                   os.environ.get('ALLOWED_ORIGINS').split(','))

    def secret_key(self):
        return "hiso secret"

config = Config()
