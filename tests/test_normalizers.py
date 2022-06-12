from unittest import TestCase

from ddt import data, ddt, unpack

from matn.normalizers import (
    clean_text,
    diacritic_removal,
    letter_normalization,
    punctuation_removal,
    tatweel_removal,
)


@ddt
class TestOrthographicNormalization(TestCase):
    @data(
        {"value": "", "expected": ""},
        {"value": None, "expected": None},
        {"value": "جميل", "expected": "جميل"},
        {"value": "ـجميل", "expected": "جميل"},
        {"value": "جـمـيـل", "expected": "جميل"},
        {"value": "جميلـ", "expected": "جميل"},
        {"value": "ــــ", "expected": ""},
    )
    @unpack
    def test_tatweel_removal(self, value, expected):
        self.assertEqual(expected, tatweel_removal(value))

    @data(
        {"value": "", "expected": ""},
        {"value": None, "expected": None},
        {"value": "جميل", "expected": "جميل"},
        {"value": "جُميل", "expected": "جميل"},
        {"value": "جَمِيْلٌ", "expected": "جميل"},
        {"value": "جميلٌ", "expected": "جميل"},
        {"value": "جَمِيْلٌ", "expected": "جميل"},
    )
    @unpack
    def test_diacritic_removal(self, value, expected):
        self.assertEqual(expected, diacritic_removal(value))

    @data(
        {"value": "", "expected": ""},
        {"value": None, "expected": None},
        {"value": "مستشفى", "expected": "مستشفى"},
        {"value": "أحمد إبراهيم", "expected": "احمد ابراهيم"},
        {"value": "جميلة", "expected": "جميله"},
        {"value": "لؤلؤ", "expected": "لءلء"},
        {"value": "أرجئ", "expected": "ارجء"},
    )
    @unpack
    def test_letter_normalization_normal(self, value, expected):
        self.assertEqual(expected, letter_normalization(value))

    @data(
        {"value": "", "expected": ""},
        {"value": None, "expected": None},
        {"value": "مستشفى", "expected": "مستشفي"},
        {"value": "أحمد إبراهيم", "expected": "احمد ابراهيم"},
        {"value": "جميلة", "expected": "جميله"},
        {"value": "لؤلؤ", "expected": "لءلء"},
        {"value": "أرجئ", "expected": "ارجء"},
    )
    @unpack
    def test_letter_normalization_egyptian(self, value, expected):
        self.assertEqual(expected, letter_normalization(value, egyptian=True))

    @data(
        {"value": "", "expected": ""},
        {"value": None, "expected": None},
        {"value": "،.(*", "expected": ""},
        {"value": "أحمد", "expected": "أحمد"},
        {"value": "يا عليّ، استذكر دروسك.", "expected": "يا عليّ استذكر دروسك"},
    )
    @unpack
    def test_punctuation_removal(self, value, expected):
        self.assertEqual(expected, punctuation_removal(value))

    @data(
        {"value": "", "expected": ""},
        {"value": None, "expected": None},
        {"value": "     ", "expected": ""},
        {"value": "     أحمد", "expected": "أحمد"},
        {"value": "     أحمد     ", "expected": "أحمد"},
        {"value": "أحمد      ", "expected": "أحمد"},
        {"value": "،.(*", "expected": ""},
        {"value": "dsafasdf", "expected": ""},
        {"value": "sdأcdحbbمaaدaa", "expected": "أحمد"},
    )
    @unpack
    def test_clean_text(self, value, expected):
        self.assertEqual(expected, clean_text(value))
