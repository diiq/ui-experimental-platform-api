from __future__ import absolute_import

from flask.ext.testing import TestCase as TC
import json
import itsdangerous

from app import app
from app.db import db
from app.models import User
from mock_data.seeds import plant_seed_file_relative


class TestCase(TC):
    seed_file = None
    seed_files = None

    def create_app(self):
        app.config['TESTING'] = True
        app.signer = itsdangerous.URLSafeSerializer(
            "sosupersecretomgyoullneverguess")

        return app

    def setUp(self):
        db.create_all()
        self.seed()

    def tearDown(self):
        db.session.commit()
        db.session.close_all()
        db.drop_all()

    def json_post(self, _url, **kwargs):
        return self.client.post(
            _url,
            data=json.dumps(kwargs),
            headers={
                'Content-Type': "application/json"
            })

    def json_put(self, _url, **kwargs):
        return self.client.put(
            _url,
            data=json.dumps(kwargs),
            headers={
                'Content-Type': "application/json"
            })

    def json_patch(self, _url, **kwargs):
        return self.client.patch(
            _url,
            data=json.dumps(kwargs),
            headers={
                'Content-Type': "application/json"
            })

    def seed(self):
        if self.seed_file:
            plant_seed_file_relative(self.seed_file)
        if self.seed_files:
            for seed_file in self.seed_files:
                plant_seed_file_relative(seed_file)

    def login(self):
        if not User.filter_by(email="sam@example.com"):
            plant_seed_file_relative("login_seeds.yaml")
        self.json_post("api/v1/auth",
                       email="sam@example.com",
                       password="unsecure")
