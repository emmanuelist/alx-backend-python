#!/usr/bin/env python3

"""
Utils Module
------------

This module contains utility functions for working with nested dictionaries.

Functions:
    access_nested_map: Access nested values in a dictionary
    using a tuple ofkeys.
"""

import unittest
from unittest.mock import Mock, patch

from parameterized import parameterized

from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    Test cases for the access_nested_map function.

    The access_nested_map function allows you to access nested
    values in a dictionary using a tuple of keys.

    Args:
        nested_map (dict): The dictionary to access.
        path (tuple): A tuple of keys to access the nested value.

    Returns:
        The value at the specified path in the dictionary.
    """

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test that the access_nested_map function returns the expected value.

        Args:
            nested_map (dict): The dictionary to access.
            path (tuple): A tuple of keys to access the nested value.
            expected: The expected value at the specified path.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([({}, ("a",)), ({"a": 1}, ("a", "b"))])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Test that the access_nested_map function raises a KeyError when
        the path is invalid.

        Args:
            nested_map (dict): The dictionary to access.
            path (tuple): A tuple of keys to access the nested value.
        """
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception.args[0]), str(path[-1]))


class TestGetJson(unittest.TestCase):
    """
    Test cases for the get_json function.
    The get_json function fetches JSON data from a given URL.
    Args:
        url (str): The URL to fetch the JSON data from.

    Returns:
    The JSON data fetched from the URL.
    """


@parameterized.expand(
    [
        ("http://example.com", {"payload": True}),
        ("http://example.com", {"payload": False}),
    ]
)
def test_get_json(self, test_url, test_payload):
    """
    Test that the get_json function returns the expected JSON data.

    Args:
        test_url (str): The URL to fetch the JSON data from.
        test_payload (dict): The expected JSON data fetched from the URL.
    """
    mock_response = Mock()
    mock_response.json.return_value = test_payload

    with patch("utils.requests.get") as mock_get:
        mock_get.return_value = mock_response
        self.assertEqual(get_json(test_url), test_payload)


class TestMemoize(unittest.TestCase):
    """
    Test cases for the memoize function.

    The memoize function caches the results of a function
    so that it does not have to be recomputed.
    """

    class TestClass:
        def a_method(self):
            return 42

        @memoize
        def a_property(self):
            return self.a_method()

    def test_memoize(self):
        """
        Test that the memorize decorator caches the result
        of a property.
        """
        with patch.object(self.TestClass,
                          "a_method", return_value=42) as mock_method:
            test_instance = self.TestClass()
            self.assertEqual(test_instance.a_property, 42)
            self.assertEqual(test_instance.a_property, 42)
            mock_method.assert_called_once()
