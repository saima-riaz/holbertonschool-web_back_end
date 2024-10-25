#!/usr/bin/env python3
""" File for testing client.GithubOrgClient """

import unittest
from unittest.mock import patch
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


class TestGithubOrgClient(unittest.TestCase):
    """ Test that json can be got """

    @parameterized.expand([
        ("google", {"google": True}),
        ("abc", {"abc": True})
    ])
    @patch('client.get_json')
    def test_org(self, org, expected, get_patch):
        """ Test the org of the client """
        get_patch.return_value = expected
        x = GithubOrgClient(org)
        self.assertEqual(x.org, expected)
        get_patch.assert_called_once_with("https://api.github.com/orgs/" + org)

    def test_public_repos_url(self):
        """ Test that _public_repos_url returns the expected result """
        test_url = "https://api.github.com/orgs/google/repos"
        payload = {"repos_url": test_url}

        with patch.object(GithubOrgClient, 'org', return_value=payload):
            client = GithubOrgClient("google")
            result = client._public_repos_url
            self.assertEqual(result, test_url)

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test the public_repos method"""
        mock_repos = [{"name": "repo1"}, {"name": "repo2"}]
        mock_get_json.return_value = mock_repos
        test_url = "https://api.github.com/orgs/google/repos"

        with patch.object(
            GithubOrgClient, '_public_repos_url', new_callable=lambda: test_url
        ):
            client = GithubOrgClient("google")
            repos = client.public_repos()

            # Assert the returned list of repo names
            self.assertEqual(repos, ["repo1", "repo2"])

            # Check if _public_repos_url and get_json were each called once
            mock_get_json.assert_called_once_with(test_url)
            self.assertEqual(mock_get_json.call_count, 1)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test the has_license method"""
        client = GithubOrgClient("google")
        result = client.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class([
    {"org_payload": org_payload, "repos_payload": repos_payload,
     "expected_repos": expected_repos, "apache2_repos": apache2_repos}
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient.public_repos method"""

    @classmethod
    def setUpClass(cls):
        """Set up a patcher for requests.get with fixtures"""
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        # Define the side_effect function for the mock response
        def side_effect(url):
            if url == "https://api.github.com/orgs/google":
                return cls.MockResponse(cls.org_payload)
            elif url == "https://api.github.com/orgs/google/repos":
                return cls.MockResponse(cls.repos_payload)
            return None

        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """Stop the patcher for requests.get"""
        cls.get_patcher.stop()

    class MockResponse:
        """Mock response to simulate `requests.get().json()`"""
        def __init__(self, json_data):
            self.json_data = json_data

        def json(self):
            return self.json_data

    def test_public_repos(self):
        """Test the public_repos method"""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Test the public_repos method with license filter"""
        client = GithubOrgClient("google")
        self.assertEqual(
            client.public_repos(license="apache-2.0"), self.apache2_repos
        )


if __name__ == "__main__":
    unittest.main()
