from unittest import TestCase

from matn.special_articles import ADDED_LETTERS, DEFINITE_ARTICLES


class TestSpecialArticles(TestCase):
    def test_definite_articles(self):
        self.assertEqual(
            DEFINITE_ARTICLES,
            (
                "ال",
                "وال",
                "بال",
                "كال",
                "فال",
            ),
        )

    def test_added_letter(self):
        self.assertEqual(
            ADDED_LETTERS,
            (
                "س",
                "أ",
                "ل",
                "ت",
                "م",
                "و",
                "ن",
                "ي",
                "ه",
                "ا",
            ),
        )
