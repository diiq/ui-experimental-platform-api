import datetime
from app.db import db, Model


class Ticket(Model, db.Model):
    __tablename__ = 'tickets'

    id = db.Column(
        db.Integer,
        db.Sequence('tickets_id_seq'),
        primary_key=True)
    subject = db.Column(db.String)
    description = db.Column(db.String)

    public_attributes = [
        'id',
        'subject',
        'description',
    ]

    str_attributes = [
        'id',
        'subject',
    ]


class TicketQuery(db.Query):
    pass

Ticket.query_class = TicketQuery
