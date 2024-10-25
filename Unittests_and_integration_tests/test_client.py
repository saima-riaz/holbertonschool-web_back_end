#!/usr/bin/env python3
""" File for testing client.GithubOrgClient """

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


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
        get_patch.assert_called_once_with("https://api.github.com/orgs/"+org)

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


if __name__ == "__main__":
    unittest.main()
