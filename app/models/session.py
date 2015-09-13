import datetime
from sqlalchemy.dialects.postgresql import JSON

from app.db import db, Model
from record import Record

##
# A Session represents one contiguous block of a single user
# participating in a single experiment. Longer experiments may require
# multiple sessions.
#
class Session(Model, db.Model):
    __tablename__ = 'sessions'
    id = db.Column(
        db.Integer,
        db.Sequence('sessions_id_seq'),
        primary_key=True)

    experiment_id = db.Column(
        db.Integer,
        db.ForeignKey("experiments.id"))
    participation_id = db.Column(
        db.Integer,
        db.ForeignKey("participations.id", ondelete="CASCADE"))

    created_at = db.Column(db.DateTime(timezone=True),
                           default=datetime.datetime.now())

    records = db.relationship(
        Record,
        backref=db.backref("session"),
        lazy="dynamic",
        query_class=Record.query_class)

    public_attributes = [
        'id',
    ]


class SessionQuery(db.Query):
    pass


Session.query_class = SessionQuery
