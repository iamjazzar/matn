from unittest import TestCase

from ddt import ddt, file_data

from matn.counters import char_count, jummal, word_count


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


@ddt
class TestWordCount(TestCase):
    @file_data("data/test_data_word_count_normal.yaml")
    def test_normal(self, text, expected):
        self.assertEqual(expected, word_count(text))

    @file_data("data/test_data_word_count_split_badama.yaml")
    def test_split_badama(self, text, expected):
        self.assertEqual(expected, word_count(text, split_badama=True))


@ddt
class TestCharCount(TestCase):
    @file_data("data/test_data_char_count_normal.yaml")
    def test_normal(self, text, expected):
        self.assertEqual(expected, char_count(text))

    @file_data("data/test_data_char_count_hamza_madda.yaml")
    def test_hamza_madda(self, text, expected):
        self.assertEqual(expected, char_count(text, hamza_madda=True))

    @file_data("data/test_data_char_count_include_spaces.yaml")
    def test_include_spaces(self, text, expected):
        self.assertEqual(expected, char_count(text, include_spaces=True))
