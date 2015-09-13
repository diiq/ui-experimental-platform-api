import datetime
from sqlalchemy.dialects.postgresql import JSON

from app.db import db, Model


class Session(Model, db.Model):
    __tablename__ = 'sessions'
    id = db.Column(
        db.Integer,
        db.Sequence('sessions_id_seq'),
        primary_key=True)

    participation_id = db.Column(
        db.Integer,
        db.ForeignKey("participations.id", ondelete="CASCADE"))

    created_at = db.Column(db.DateTime(timezone=True),
                           default=datetime.datetime.now())
    primaryEvents = db.Column(JSON)
    allEvents = db.Column(JSON)

    public_attributes = [
        'id',
    ]


class SessionQuery(db.Query):
    pass


Session.query_class = SessionQuery
