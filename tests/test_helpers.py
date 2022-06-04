from unittest import TestCase

from ddt import data, ddt, unpack

from matn.helpers import pattern_sub


@ddt
class TestPatternSub(TestCase):
    @data(
        ["some text goes here", {"goes": ""}, "some text  here"],
        ["some text goes here", {"goes": "comes"}, "some text comes here"],
        ["some text goes here", {" ": "|"}, "some|text|goes|here"],
    )
    @unpack
    def test_one_replacement(self, text, replacements, expected):
        self.assertEqual(expected, pattern_sub(text, replacements))

    @data(
        ["some text goes here", {"text": "", "goes": ""}, "some   here"],
        ["some text goes here", {"text": "", "goes": "comes"}, "some  comes here"],
        ["some text goes here", {"text": "data", "goes": ""}, "some data  here"],
        [
            "some text goes here",
            {"text": "data", "goes": "come"},
            "some data come here",
        ],
    )
    @unpack
    def test_multiple_replacements(self, text, replacements, expected):
        self.assertEqual(expected, pattern_sub(text, replacements))

    @data(
        ["some (text) goes here", {"(": "{", ")": "}"}, "some {text} goes here"],
        ["some (text) goes here", {"goes here": "<>"}, "some (text) <>"],
        [
            "(. , + , * , ? , ^ , $ , ( , ) , [ , ] , { , } , | , \\)",
            {"* , ? , ^": "* , * , *"},
            "(. , + , * , * , * , $ , ( , ) , [ , ] , { , } , | , \\)",
        ],
    )
    @unpack
    def test_replacements_special_characters(self, text, replacements, expected):
        self.assertEqual(expected, pattern_sub(text, replacements))

    @data(
        [
            "نَعَمْ سَرَى طَيْفُ مَنْ أَهْوَى فَأَرَّقَنِي",
            {"فَأَرَّقَنِي": ""},
            "نَعَمْ سَرَى طَيْفُ مَنْ أَهْوَى ",
        ],
        [
            "نَعَمْ سَرَى طَيْفُ مَنْ أَهْوَى فَأَرَّقَنِي",
            {"فَأَرَّقَنِي": "فحيرني"},
            "نَعَمْ سَرَى طَيْفُ مَنْ أَهْوَى فحيرني",
        ],
        [
            "نَعَمْ سَرَى طَيْفُ",
            {"نَعَمْ سَرَى طَيْفُ": "وَالحُبُّ يَعْتَرِضُ"},
            "وَالحُبُّ يَعْتَرِضُ",
        ],
    )
    @unpack
    def test_multiple_replacements_arabic(self, text, replacements, expected):
        self.assertEqual(expected, pattern_sub(text, replacements))
