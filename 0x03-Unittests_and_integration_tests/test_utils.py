#!/usr/bin/env python3
"""Tests for utils.py="""

import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """Tests for access_nested_map."""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map with different inputs."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, Emessage):
        """Test access_nested_map with exceptions."""
        with self.assertRaises(Emessage):
            self.assertEqual(access_nested_map(nested_map, path))


class TestGetJson(unittest.TestCase):
    """Tests for get_json."""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests.get')
    def test_get_json(self, url, payload, mock_get):
        """Test get_json with different inputs."""
        mock_get.return_value = Mock(json=lambda: payload)
        self.assertEqual(get_json(url), payload)


class TestMemoize(unittest.TestCase):
    """Tests for memoize."""
    def test_memoize(self):
        """Test memoize."""
        class TestClass:
            """Test class."""
            def a_method(self):
                """A method."""
                return 42

            @memoize
            def a_property(self):
                """A property."""
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_method:
            test_object = TestClass()
            result1 = test_object.a_property()
            result2 = test_object.a_property()

            mock_method.assert_called_once()

            self.assertEqual(result1, result2)


if __name__ == '__main__':
    unittest.main()
