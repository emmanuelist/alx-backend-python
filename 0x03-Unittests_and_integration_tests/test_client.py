#!/usr/bin/env python3
import unittest
from unittest.mock import PropertyMock, patch

from parameterized import parameterized

from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Test cases for the GithubOrgClient class
    """

    @parameterized.expand([("google",), ("abc",)])
    @patch("client.get_json", return_value={"login": "google"})
    def test_org(self, org_name, mock_get_json):
        """
        Test that GithubOrgClient.org return the correct value
        """
        client = GithubOrgClient(org_name)
        result = client.org
        self.assertEqual(result, {"login": "google"})
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

    def test_public_repos_url(self):
        """
        Test that GithubOrgClient.public_repos_url return the correct value
        """
        with patch.object(GithubOrgClient, "org",
                          new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {
                "repos_url": "https://api.github.com/orgs/google/repos"
            }
            client = GithubOrgClient("google")
            result = client._public_repos_url
            self.assertEqual(result,
                             "https://api.github.com/orgs/google/repos")
