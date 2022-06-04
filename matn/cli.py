import argparse

from matn import jummal


def get_args():
    parser = argparse.ArgumentParser(
        description="A mathmatical tool for Arabic counting systems."
    )
    parser.add_argument(
        "processor",
        choices=["jummal"],
        help="the processor to be applied on the given string.",
    )
    parser.add_argument(
        "text",
        type=str,
        help="The string to be counted",
    )

    return parser.parse_args()


def main():
    args = get_args()
    print(jummal(args.text))


if __name__ == "__main__":
    exit(main())
