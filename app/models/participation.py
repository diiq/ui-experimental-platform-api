import datetime

from app.db import db, Model
from session import Session


class Participation(Model, db.Model):
    __tablename__ = 'participations'
    id = db.Column(
        db.Integer,
        db.Sequence('participations_id_seq'),
        primary_key=True)

    experiment_id = db.Column(
        db.Integer,
        db.ForeignKey("experiments.id", ondelete="CASCADE"))
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id", ondelete="CASCADE"))

    created_at = db.Column(db.DateTime(timezone=True),
                           default=datetime.datetime.now())
    sessions_completed = db.Column(db.Integer, nullable=False, default=0)

    sessions = db.relationship(
        Session,
        backref=db.backref("participation"),
        lazy="joined",
        passive_deletes=True,
        query_class=Session.query_class)

    public_attributes = [
        'id',
        'sessions_completed',
        'started',
        'complete'
    ]

    def started(self):
        return self.sessions_completed > 0

    def complete(self):
        return self.sessions_completed == self.experiment.session_count


class ParticipationQuery(db.Query):
    pass


Participation.query_class = ParticipationQuery
