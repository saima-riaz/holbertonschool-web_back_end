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


if __name__ == "__main__":
    unittest.main()
