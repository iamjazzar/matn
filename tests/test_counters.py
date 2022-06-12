from unittest import TestCase

from ddt import ddt, file_data

from matn.counters import char_count, jummal, word_count


@ddt
class TestJummal(TestCase):
    @file_data("data/test_data_jummal.yaml")
    def test_normal(self, text, expected, **kwargs):
        self.assertEqual(expected, jummal(text))

    @file_data("data/test_data_jummal.yaml")
    def test_hamza(self, text, expected_hamza, **kwargs):
        self.assertEqual(expected_hamza, jummal(text, use_hamza=True))

    @file_data("data/test_data_jummal.yaml")
    def test_tarkeeb(self, text, expected_tarkeeb, **kwargs):
        self.assertEqual(expected_tarkeeb, jummal(text, use_tarkeeb=True))

    @file_data("data/test_data_jummal.yaml")
    def test_tarkeeb_hamza(self, text, expected_tarkeeb_hamza, **kwargs):
        self.assertEqual(
            expected_tarkeeb_hamza, jummal(text, use_hamza=True, use_tarkeeb=True)
        )

    @file_data("data/test_data_jummal.yaml")
    def test_normalized_hamza(self, text, expected_normalized_hamza, **kwargs):
        self.assertEqual(expected_normalized_hamza, jummal(text, normalize_hamza=True))


@ddt
class TestWordCount(TestCase):
    @file_data("data/test_data_word_count.yaml")
    def test_normal(self, text, expected, **kwargs):
        self.assertEqual(expected, word_count(text))

    @file_data("data/test_data_word_count.yaml")
    def test_split_badama(self, text, expected_split_badama, **kwargs):
        self.assertEqual(expected_split_badama, word_count(text, split_badama=True))


@ddt
class TestCharCount(TestCase):
    @file_data("data/test_data_char_count.yaml")
    def test_normal(self, text, expected, **kwargs):
        self.assertEqual(expected, char_count(text))

    @file_data("data/test_data_char_count.yaml")
    def test_hamza_madda(self, text, expected_hamza_madda, **kwargs):
        self.assertEqual(expected_hamza_madda, char_count(text, hamza_madda=True))

    @file_data("data/test_data_char_count.yaml")
    def test_include_spaces(self, text, expected_include_spaces, **kwargs):
        self.assertEqual(expected_include_spaces, char_count(text, include_spaces=True))
