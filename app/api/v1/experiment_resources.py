from resource import Resource
from v1_api import api
from app.models import Experiment


@api.resource("/api/v1/experiments")
class ExperimentsResource(Resource):
    def get(self):
        return {
            'experiments': Experiment.query.all()
        }
