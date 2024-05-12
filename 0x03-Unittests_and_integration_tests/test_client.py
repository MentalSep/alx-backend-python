#!/usr/bin/env python3
"""Tests for client.py"""
import unittest
from unittest.mock import patch
import unittest.mock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Tests for GithubOrgClient."""
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test org."""
        client = GithubOrgClient(org_name)
        client.org()
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

    def test_public_repos(self):
        """Test public_repos."""
        with patch('client.GithubOrgClient.repos_payload',
                   new_callable=unittest.mock.PropertyMock) as payload:
            payload.return_value = {'repos_url':
                                    'https://api.github.com/orgs/google/repos'}
            client = GithubOrgClient('google')
            self.assertEqual(client._public_repos_url,
                             'https://api.github.com/orgs/google/repos')


if __name__ == '__main__':
    unittest.main()
