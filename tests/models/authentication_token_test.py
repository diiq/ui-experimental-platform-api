from tests.test_case import TestCase
from app.models import AuthenticationToken


class AuthenticationTokenTests(TestCase):
    def test_generate_token(self):
        token = AuthenticationToken()
        assert(token.token)

        token2 = AuthenticationToken()
        self.assertNotEqual(token2, token)
