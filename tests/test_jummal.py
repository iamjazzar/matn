from unittest import TestCase

from ddt import ddt, file_data

from matn.counters import jummal


@ddt
class TestJummal(TestCase):
    @file_data("data/test_data_jummal_normal.yaml")
    def test_normal(self, text, expected):
        self.assertEqual(expected, jummal(text))

    @file_data("data/test_data_jummal_hamza.yaml")
    def test_hamza(self, text, expected):
        self.assertEqual(expected, jummal(text, use_hamza=True))

    @file_data("data/test_data_jummal_tarkeeb.yaml")
    def test_tarkeeb(self, text, expected):
        self.assertEqual(expected, jummal(text, use_tarkeeb=True))

    @file_data("data/test_data_jummal_tarkeeb_hamza.yaml")
    def test_tarkeeb_hamza(self, text, expected):
        self.assertEqual(expected, jummal(text, use_hamza=True, use_tarkeeb=True))

    @file_data("data/test_data_jummal_normalized_hamza.yaml")
    def test_tarkeeb_normalized_hamza(self, text, expected):
        self.assertEqual(expected, jummal(text, normalize_hamza=True))
