"""seeds.plant_all_seeds() loops over all yaml files in
mock_data/seeds, and MERGES the data it finds into the database.

WARNING: MERGING CAN AND WILL CHANGE EXISTING RECORDS IN YOUR
DATABASE. IT IS RECCOMMENDED YOU ONLY SEED EMPTY DATABASES.

"""

import yaml
import os.path
import glob
import flask_sqlalchemy

from app.db import db
from app import models


def get_model(name):
    if not hasattr(models, name):
        raise TypeError("Model not found: %s" % name)
    return getattr(models, name)


def seed_files():
    dir = os.path.abspath(os.path.dirname(__file__))
    for name in glob.glob(dir + "/*.yaml"):
        with open(name) as f:
            yield(f.read())


def plant_all_seeds():
    for filename in seed_files():
        plant_seed_file(filename)
    db.session.commit()


def plant_seed_file(filename):
    with open(filename) as seeds:
        for seed in yaml.load(seeds):
            plant_seed(seed)
            db.session.commit()
    for model in models.all_models:
        if hasattr(model, 'reset_id_counter'):
            model.reset_id_counter()


def plant_seed_file_relative(filename):
    dir = os.path.abspath(os.path.dirname(__file__))
    filename = os.path.join(dir, filename)
    plant_seed_file(filename)


def plant_seed(model_dict):
    model_name = model_dict.pop('model')
    Model = get_model(model_name)
    model = Model(**model_dict)
    if isinstance(Model, flask_sqlalchemy._BoundDeclarativeMeta):
        db.session.merge(model)
