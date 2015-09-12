from tests.test_case import TestCase


class UserResourceTests(TestCase):
    seed_file = "login_seeds.yaml"

    def test_successful_signup(self):
        response = self.json_post(
            "api/v1/users",
            email="steve@example.com",
            password="unsecure")
        self.assertEqual(response.status_code, 200)

    def test_unsuccessful_signup(self):
        response = self.json_post(
            "api/v1/users",
            email="sam@example.com",
            password="very-secure")
        self.assertEqual(response.status_code, 422)
        self.assertEqual(
            response.json['message'],
            "You've already signed up with that email!")
