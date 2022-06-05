from unittest import TestCase

from ddt import ddt, file_data

from matn.helpers import pattern_sub


@ddt
class TestPatternSub(TestCase):
    @file_data("data/test_data_pattern_sub.yaml")
    def test_one_replacement(self, text, replacements, expected):
        self.assertEqual(expected, pattern_sub(text, replacements))
