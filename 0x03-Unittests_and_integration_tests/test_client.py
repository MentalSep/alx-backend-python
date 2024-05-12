#!/usr/bin/env python3
"""Tests for client.py"""
import unittest
from unittest.mock import patch, MagicMock
import unittest.mock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


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

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test has_license."""
        self.assertEqual(GithubOrgClient.has_license(repo, license_key),
                         expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient"""

    @classmethod
    def setUpClass(cls):
        """Set up class"""
        cls.get_patcher = patch('requests.get')

        cls.mock_get = cls.get_patcher.start()
        cls.mock_get.side_effect = [
            MagicMock(json=lambda: cls.org_payload),
            MagicMock(json=lambda: cls.repos_payload)
        ]

    @classmethod
    def tearDownClass(cls):
        """Tear down class"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test public_repos"""
        github_org_client = GithubOrgClient('testorg')

        repos = github_org_client.public_repos()

        self.assertEqual(repos, self.expected_repos)


if __name__ == '__main__':
    unittest.main()
