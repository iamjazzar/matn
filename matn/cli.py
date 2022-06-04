import argparse

from matn.counters import jummal


def get_args():
    parser = argparse.ArgumentParser(description=("Arabic text processor tool."))

    subparsers = parser.add_subparsers(
        help="the processor to be applied on the given string"
    )

    parser_jummal = subparsers.add_parser("jummal", help="Jummal counter")
    parser_jummal.add_argument(
        "--use-hamza", "-z", action="store_true", help="count hamza as an alef."
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

    parser.add_argument(
        "text",
        type=str,
        help="the string to process",
    )

    return parser.parse_args()


def main():
    args = get_args()
    print(jummal(args.text, use_hamza=args.use_hamza, use_tarkeeb=args.use_tarkeeb))


if __name__ == "__main__":
    exit(main())
