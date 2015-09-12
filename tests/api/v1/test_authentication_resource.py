from tests.test_case import TestCase


class AuthenticationResourseTests(TestCase):
    seed_file = "login_seeds.yaml"

    def test_successful_login(self):
        response = self.json_post(
            "/api/v1/auth",
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
