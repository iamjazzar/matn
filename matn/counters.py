from matn import elements as ase
from matn.normalizers import clean_text

jummal_mappings = {
    "ا": 1,
    "ء": 1,  # Hamza
    "أ": 1,  # Hamza on alef maftoha
    "إ": 1,  # Hamza on alef maksora
    "ب": 2,
    "ج": 3,
    "د": 4,
    "ه": 5,
    "ة": 5,  # Teh marbota
    "و": 6,
    "ؤ": 6,  # Hamza on waw
    "ز": 7,
    "ح": 8,
    "ط": 9,
    "ي": 10,
    "ى": 10,  # Alef maksora
    "ئ": 10,  # Hamza on yeh
    "ك": 20,
    "ل": 30,
    "م": 40,
    "ن": 50,
    "س": 60,
    "ع": 70,
    "ف": 80,
    "ص": 90,
    "ق": 100,
    "ر": 200,
    "ش": 300,
    "ت": 400,
    "ث": 500,
    "خ": 600,
    "ذ": 700,
    "ض": 800,
    "ظ": 900,
    "غ": 1_000,
}


def jummal(
    text: str,
    use_hamza: bool = False,
    use_tarkeeb: bool = False,
    normalize_hamza: bool = False,
) -> int:
    """Get the decimal alphanumeric code of a given string.

    Or Abjad numerals, a decimal alphabetic numeral system/alphanumeric code,
    in which the 28 letters of the Arabic alphabet are assigned numerical
    values. They have been used in the Arabic-speaking world since before
    the eighth century when positional Arabic numerals were adopted.

    Args:
        text (str): Text to get its jummal.
        use_hamza (bool, optional): Count hamza as an alef. Defaults to False.
        use_tarkeeb (bool, optional): Used to express the numbers from 2000 to
            1,000,000, using the rule based on the letter "غ". The rule says: any
            character that comes before "غ" its value will be multiplied with
            1000 instead of accumalated to it. Defaults to False.
        normalize_hamza (bool, optional): Treat all hamza forms as a regular alef
            instead of the letter it appears on. Defaults to False.

    Returns:
        int: The jummal count of the given string
    """
    text = clean_text(text)

    count = 0
    total = len(text)

    skip = False
    for i, char in enumerate(text):
        if skip:
            skip = False
            continue

        if not use_hamza and char == ase.HAMZA:
            continue

        if use_tarkeeb and not char.isspace() and i + 1 < total and text[i + 1] == "غ":
            count += 1000 * jummal_mappings[char]
            skip = True
            continue

        if normalize_hamza and char in ase.HAMZA_LETTERS:
            count += 1
            continue

        count += jummal_mappings.get(char, 0)

    return count
