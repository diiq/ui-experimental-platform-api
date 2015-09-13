from tests.test_case import TestCase


class ExperimentResourceTests(TestCase):
    seed_files = ["login_seeds.yaml", "experiments_seeds.yaml"]

    def test_experiments_get(self):
        self.login()
        response = self.client.get("api/v1/experiments")
        experiments = response.json['experiments']
        self.assertEqual(len(experiments), 1)
