from resource import Resource
from v1_api import api
from app.models import Ticket


@api.resource("/api/v1/status")
class StatusResource(Resource):
    def get(self):

        print Ticket.query.first()

        return {
            'ok': True
        }
