import datetime

from app.db import db, Model
from participation import Participation
from session import Session
from record import Record


class Experiment(Model, db.Model):
    __tablename__ = 'experiments'
    id = db.Column(
        db.Integer,
        db.Sequence('experiments_id_seq'),
        primary_key=True)

    created_at = db.Column(db.DateTime(timezone=True),
                           default=datetime.datetime.now())

    title = db.Column(db.String, nullable=False, unique=True)
    session_duration = db.Column(db.Integer, nullable=False)
    session_count = db.Column(db.Integer, nullable=False)
    # 'slug' is a url-safe string used to identify the experiment client-side
    slug = db.Column(db.String, nullable=False)
    has_results = db.Column(db.Boolean, nullable=False, default=False)
    requires_keyboard = db.Column(db.Boolean, nullable=False, default=False)
    requires_mouse = db.Column(db.Boolean, nullable=False, default=False)
    requires_touch = db.Column(db.Boolean, nullable=False, default=False)

    participations = db.relationship(
        Participation,
        backref=db.backref("experiment", lazy="joined"),
        lazy="dynamic",
        passive_deletes=True,
        query_class=Participation.query_class)

    sessions = db.relationship(
        Session,
        backref=db.backref("experiment"),
        lazy="dynamic",
        query_class=Session.query_class)

    records = db.relationship(
        Record,
        backref=db.backref("experiment"),
        lazy="dynamic",
        query_class=Record.query_class)

    public_attributes = [
        'id',
        'title',
        'session_duration',
        'session_count',
        'slug',
        'has_results',
        'requires_keyboard',
        'requires_mouse',
        'requires_touch',
    ]


class ExperimentQuery(db.Query):
    pass


Experiment.query_class = ExperimentQuery
