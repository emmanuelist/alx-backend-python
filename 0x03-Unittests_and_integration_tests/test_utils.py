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

from parameterized import parameterized

from utils import access_nested_map


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
