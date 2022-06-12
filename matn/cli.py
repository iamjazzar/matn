import argparse

from matn.counters import char_count, jummal, word_count


def get_args():  # pragma: no cover
    parser = argparse.ArgumentParser(description=("Arabic text processor tool."))

    subparsers = parser.add_subparsers(
        dest="processor", help="the processor to be applied on the given string"
    )

    parser_jummal = subparsers.add_parser("jummal", help="Jummal counter")
    parser_jummal.add_argument(
        "--use-hamza", "-z", action="store_true", help="count hamza as an alef."
    )
    parser_jummal.add_argument(
        "--normalize-hamza",
        "-n",
        action="store_true",
        help=(
            "Treat all hamza forms as a regular alef instead of the "
            "letter it appears on. Defaults to False."
        ),
    )
    parser_jummal.add_argument(
        "--use-tarkeeb",
        "-t",
        action="store_true",
        help=(
            "the tarkeeb rule based on the letter 'غ' to express "
            "numbers from 2,000 to 1,000,000."
        ),
    )

    parser_wc = subparsers.add_parser("wc", help="Words counter")
    parser_wc.add_argument(
        "--split-badama",
        "-s",
        action="store_true",
        help="wether to count the word بعدما as two words بعد and ما.",
    )

    parser_cc = subparsers.add_parser("cc", help="Characters counter")
    parser_cc.add_argument(
        "--hamza-madda",
        "-m",
        action="store_true",
        help="indicates if spaces should be included in the count.",
    )
    parser_cc.add_argument(
        "--include-spaces",
        "-s",
        action="store_true",
        help="consider the hamza madda (أٓ) two characters.",
    )

    parser.add_argument(
        "text",
        type=str,
        help="the string to process",
    )

    return parser, parser.parse_args()


def main():
    parser, args = get_args()

    if args.processor == "jummal":
        print(
            jummal(
                args.text,
                use_hamza=args.use_hamza,
                use_tarkeeb=args.use_tarkeeb,
                normalize_hamza=args.normalize_hamza,
            )
        )
    elif args.processor == "wc":
        print(word_count(args.text, split_badama=args.split_badama))
    elif args.processor == "cc":
        print(
            char_count(
                args.text,
                include_spaces=args.include_spaces,
                hamza_madda=args.hamza_madda,
            )
        )
    else:
        parser.error("Prcessor action not recognized")


if __name__ == "__main__":  # pragma: no cover
    exit(main())
