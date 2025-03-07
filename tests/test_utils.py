# Copyright (c) 2019 Red Hat, Inc.

"""Test tahrir.utils."""

import unittest

from tahrir import utils


class TestSingularize(unittest.TestCase):
    """Test the singularize() function."""

    def test_singularize_value_1(self):
        """Test that the trailing letter is returned when value is 1."""
        self.assertEqual(utils.singularize("cats", 1), "cat")


class TestMergeDicts(unittest.TestCase):
    """Test the merge_dicts() function."""

    def test_merge_dicts(self):
        dict1 = {1: "a"}
        dict2 = {2: ["b"]}
        self.assertEqual(utils.merge_dicts(dict1, dict2), {1: "a", 2: ["b"]})


class TestStrToBytes(unittest.TestCase):
    """Test the str_to_bytes() function."""

    def test_str_to_bytes_str(self):
        self.assertEqual(utils.str_to_bytes("foo"), b"foo")

    def test_str_to_bytes_bytes(self):
        self.assertEqual(utils.str_to_bytes(b"foo"), b"foo")

    def test_str_to_bytes_other(self):
        self.assertEqual(utils.str_to_bytes(["list"]), ["list"])
