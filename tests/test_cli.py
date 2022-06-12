import argparse
from unittest import TestCase
from unittest.mock import MagicMock, patch

from matn.cli import main


class TestMain(TestCase):
    @patch("matn.cli.char_count")
    @patch("matn.cli.word_count")
    @patch("matn.cli.jummal")
    @patch("matn.cli.get_args")
    def test_jummal(self, mock_get_args, mock_jummal, *args):
        class Args:
            processor = "jummal"
            text = "منشت منشس بمنشس مش"
            use_hamza = True
            use_tarkeeb = True
            normalize_hamza = False

        mock_get_args.return_value = MagicMock(), Args()

        main()

        mock_get_args.assert_called_once_with()
        mock_jummal.assert_called_once_with(
            Args.text,
            use_hamza=Args.use_hamza,
            use_tarkeeb=Args.use_tarkeeb,
            normalize_hamza=Args.normalize_hamza,
        )

        for arg in args:
            arg.assert_not_called()

    @patch("matn.cli.char_count")
    @patch("matn.cli.jummal")
    @patch("matn.cli.word_count")
    @patch("matn.cli.get_args")
    def test_word_count(self, mock_get_args, mock_word_count, *args):
        class Args:
            processor = "wc"
            text = "منشت منشس بمنشس مش"
            split_badama = True

        mock_get_args.return_value = MagicMock(), Args()
        main()

        mock_get_args.assert_called_once_with()
        mock_word_count.assert_called_once_with(
            Args.text,
            split_badama=Args.split_badama,
        )

        for arg in args:
            arg.assert_not_called()

    @patch("matn.cli.jummal")
    @patch("matn.cli.word_count")
    @patch("matn.cli.char_count")
    @patch("matn.cli.get_args")
    def test_char_count(self, mock_get_args, mock_char_count, *args):
        class Args:
            processor = "cc"
            text = "منشت منشس بمنشس مش"
            include_spaces = False
            hamza_madda = True

        mock_get_args.return_value = MagicMock(), Args()
        main()

        mock_get_args.assert_called_once_with()
        mock_char_count.assert_called_once_with(
            Args.text,
            include_spaces=Args.include_spaces,
            hamza_madda=Args.hamza_madda,
        )

        for arg in args:
            arg.assert_not_called()

    @patch("matn.cli.jummal")
    @patch("matn.cli.word_count")
    @patch("matn.cli.char_count")
    @patch("matn.cli.get_args")
    def test_unsupported_parser(self, mock_get_args, *args):
        class Args:
            processor = "wrong_value"

        parser = argparse.ArgumentParser()
        mock_get_args.return_value = parser, Args()

        with self.assertRaises(SystemExit):
            main()

        for arg in args:
            arg.assert_not_called()
