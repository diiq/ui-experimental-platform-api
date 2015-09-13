import datetime

from app.db import db, Model
from session import Session


##
# When a user decides to participate in an experiment, this is where
# we store information about that relationship.
#
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

    records = db.relationship(
        "Record",
        secondary="sessions",
        primaryjoin="Session.participation_id == Participation.id",
        secondaryjoin="Session.id == Record.session_id",
        lazy="dynamic",
        uselist=True,
        viewonly=True)

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
