from resource import Resource
from v1_api import api


@api.resource("/api/v1/status")
class StatusResource(Resource):
    def get(self):
        return {
            'ok': True
        }
