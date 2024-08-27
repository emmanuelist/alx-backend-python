#!/usr/bin/env python3
import unittest
from unittest.mock import PropertyMock, patch

import requests
from parameterized import parameterized, parameterized_class

from client import GithubOrgClient
from fixtures import apache2_repos, expected_repos, org_payload, repos_payload


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
        with patch.object(
            GithubOrgClient, "org", new_callable=PropertyMock
        ) as mock_org:
            mock_org.return_value = {
                "repos_url": "https://api.github.com/orgs/google/repos"
            }
            client = GithubOrgClient("google")
            result = client._public_repos_url
            self.assertEqual(result,
                             "https://api.github.com/orgs/google/repos")

    @patch("client.get_json", return_value=[{"name": "repo1"},
                                            {"name": "repo2"}])
    def test_public_repos(self, mock_get_json):
        """
        Test that GithubOrgClient.public_repos returns the correct
        list of repos
        """
        with patch.object(
            GithubOrgClient, "_public_repos_url", new_callable=PropertyMock
        ) as mock_public_repos_url:
            mock_public_repos_url.return_value = (
                "https://api.github.com/orgs/google/repos"
            )
            client = GithubOrgClient("google")
            result = client.public_repos()
            self.assertEqual(result, ["repo1", "repo2"])
            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/google/repos"
            )

    @parameterized.expand(
        [
            ({"license": {"key": "my_license"}}, "my_license", True),
            ({"license": {"key": "other_license"}}, "my_license", False),
        ]
    )
    def test_has_license(self, repo, license_key, expected):
        """
        Test the GithubOrgClient.has_license return the current boolean value
        on the license key
        """
        client = GithubOrgClient("google")
        result = client.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class(
    [
        {
            "org_payload": org_payload,
            "repos_payload": repos_payload,
            "expected_repos": expected_repos,
            "apache2_repos": apache2_repos,
        }
    ]
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        Set up class method to mock requests.get to return example payloads
        found in the fixtures.
        """
        cls.get_patcher = patch("requests.get",
                                side_effect=cls.mocked_requests_get)
        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """
        Tear down class method to stop the patcher.
        """
        cls.get_patcher.stop()

    @staticmethod
    def mocked_requests_get(url):
        """
        Mocked requests.get method to return the correct fixtures for the
        various values of url.
        """
        if url == "https://api.github.com/orgs/google":
            return MockResponse(org_payload)
        elif url == "https://api.github.com/orgs/google/repos":
            return MockResponse(repos_payload)
        return MockResponse(None, 404)


class MockResponse:
    """
    Mock response class to simulate requests.Response
    """

    def __init__(self, json_data, status_code=200):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data
