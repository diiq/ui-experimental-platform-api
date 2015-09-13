import datetime
from sqlalchemy.dialects.postgresql import JSON

from app.db import db, Model


##
# A record is the atomic unit of an experiment. It represents a single
# user participating in an experiment exactly once. A session may be
# made of many records.
#
class Record(Model, db.Model):
    __tablename__ = 'records'
    id = db.Column(
        db.Integer,
        db.Sequence('records_id_seq'),
        primary_key=True)

    experiment_id = db.Column(
        db.Integer,
        db.ForeignKey("experiments.id"))
    session_id = db.Column(
        db.Integer,
        db.ForeignKey("sessions.id", ondelete="CASCADE"))

    created_at = db.Column(db.DateTime(timezone=True),
                           default=datetime.datetime.now())
    primaryEvents = db.Column(JSON)
    allEvents = db.Column(JSON)

    public_attributes = [
        'id',
    ]


class RecordQuery(db.Query):
    pass


Record.query_class = RecordQuery
