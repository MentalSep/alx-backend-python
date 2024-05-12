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

    def test_public_repos_url(self):
        """Test public_repos."""
        with patch('client.GithubOrgClient.org',
                   new_callable=unittest.mock.PropertyMock) as mock_org:
            mock_org.return_value = {"repos_url": "http://repos.url"}
            client = GithubOrgClient("example")
            self.assertEqual(client._public_repos_url, "http://repos.url")

    def test_public_repos(self):
        """Test public_repos."""
        with patch('client.GithubOrgClient.repos_payload',
                   new_callable=unittest.mock.PropertyMock) as mock_payload:
            mock_payload.return_value = [
                {"name": "a", "license": {"key": "a-key"}},
                {"name": "b", "license": {"key": "b-key"}},
            ]
            client = GithubOrgClient("example")
            self.assertEqual(client.public_repos("a-key"), ["a"])
            self.assertEqual(client.public_repos("b-key"), ["b"])
            self.assertEqual(client.public_repos(), ["a", "b"])


if __name__ == '__main__':
    unittest.main()
