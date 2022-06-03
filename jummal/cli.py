import argparse

from jummal.processor import jummal_counter


def get_args():
    parser = argparse.ArgumentParser(description="Count the jummal of a given string.")
    parser.add_argument(
        "text",
        type=str,
        help="The string to be counted",
    )

    return parser.parse_args()


def main():
    args = get_args()
    print(jummal_counter(args.text))


if __name__ == "__main__":
    exit(main())
