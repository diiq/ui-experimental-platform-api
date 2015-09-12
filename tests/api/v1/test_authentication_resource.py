from tests.test_case import TestCase


class AuthenticationResourseTests(TestCase):
    seed_file = "login_seeds.yaml"

    def test_successful_login(self):
        response = self.json_post(
            "api/v1/auth",
            email="sam@example.com",
            password="unsecure")
        self.assertEqual(response.status_code, 200)

    def test_unsuccessful_login_bad_password(self):
        response = self.json_post(
            "api/v1/auth",
            email="sam@example.com",
            password="very-secure")
        self.assertEqual(response.status_code, 403)

    def test_unsuccessful_login_bad_email(self):
        response = self.json_post(
            "api/v1/auth",
            email="steve@example.com",
            password="unsecure")
        self.assertEqual(response.status_code, 403)

    def test_successful_role_check(self):
        role = 'user'
        self.login()
        response = self.client.get(
            "api/v1/auth",
            query_string={'role': role})
        self.assertEqual(response.json['role'], role)
        self.assertEqual(response.json['authorized'], True)

    def test_unsuccessful_role_check(self):
        role = 'loser'
        self.login()
        response = self.client.get(
            "api/v1/auth",
            query_string={'role': role})
        self.assertEqual(response.json['role'], role)
        self.assertEqual(response.json['authorized'], False)

    def test_me_resource(self):
        self.login()
        response = self.client.get("api/v1/auth/me")
        self.assertEqual(response.json['email'], "sam@example.com")

    def test_auth_token(self):
        token = self.user().authentication_token
        response = self.client.get(
            "api/v1/auth/me",
            query_string={'auth': token})
        self.assertEqual(response.json['email'], "sam@example.com")
