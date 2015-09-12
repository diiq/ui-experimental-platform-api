from tests.test_case import TestCase
from app.models import User


class UserTests(TestCase):
    seed_file = "login_seeds.yaml"

    def test_roles(self):
        user = User.query.first()
        assert(user.fulfills_role('user'))
        assert(not user.fulfills_role('loser'))
