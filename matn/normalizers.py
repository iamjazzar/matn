import matn.elements as ase


def tatweel_removal(text: str) -> str:
    """Remove kashidas from string

    The Tatweel (elongation, or kashidas) is used to stretch words
    to indicate prominence or simply to force vertical justification.
    This symbol has no effect on the meaning of the word so it's
    usually normalized.

    Examples:
        - A word without Tatweel:       جميل
        - The same word with Tatweel:   جـــمـــيـــل

    Args:
        text (str): The text we need to extract the Tatweel from.

    Returns:
        str: A text without Tatweels.
    """
    if not text:
        return text

    return text.replace(ase.TATWEEL, "")


def diacritic_removal(text: str) -> str:
    """Remove diacritics from string

    Since diacritics occur so infrequently, they are considered noise
    by most researchers and are simply removed from the text.

    Examples:
        - A word without diacritics:     جميل
        - The same word with diacritics: جَمِيلٌ

    Args:
        text (str): The text that we need to extract diacritics from.

    Returns:
        str: A text without diacritics.
    """
    if not text:
        return text

    for diacritic in ase.DIACRITICS:
        text = text.replace(diacritic, "")

    return text


def punctuation_removal(text: str) -> str:
    """Remove all punctuation marks from text

    Args:
        text (str): The text to process.

    Returns:
        str: A punctuation-free text
    """
    if not text:
        return text

    for mark in ase.PUNCTUATION_MARKS:
        if mark in ase.NUMBERS_PUNCTUATION_MARKS:
            continue

        text = text.replace(mark, "")

    return text


def letter_normalization(text: str, egyptian: bool = False) -> str:
    """Normalize charactes in a given string to a standard form
    There are four letters in Arabic that are so often misspelled using
    variants that researchers find it more helpful to completely make
    these variants ambiguous (normalized).

    1. The Hamzated forms of Alif -> Alif.
    2. The Alif-Maqsura -> Ya (Only in Egypt).
    3. The Ta-Marbuta -> Ha.
    4. The non-Alif forms of Hamza -> Hamza letter.

    However, this is sometimes may be problematic. Let's take the
    name 'Ana' and the word 'Me' meaning for example, both words after
    normalization are gonna produce the same word which's not going
    to be interesting especially in named entity recognition.

     Examples:
       * Ana:
        - Correct form: آنا
        - After Normalization: انا
       * Me:
        - Correct form: أنا
        - After Normalization: انا

    Args:
        text (str): The text we want to normalize its letters.
        egyptian (bool, optional): To flag if we want to normalize the
            Alif-Maqsura. Defaults to False.

    Returns:
        str:  A letter-normalized string
    """
    if not text:
        return text

    if egyptian:
        text = text.replace(ase.ALIF_MAQSURA, "ي")

    for form in ase.ALEF_HAMZA_FORMS:
        text = text.replace(form, "ا")

    text = text.replace(ase.TA_MARBUTA, "ه")

    for form in ase.NON_ALIF_HAMZA_FORMS:
        text = text.replace(form, ase.HAMZA)

    return text


def clean_text(text: str) -> str:
    """Cleans the word by removing punctuations, diacritics, non-letter
    characters.

    Args:
        text (str): The word to clean

    Returns:
        str: A cleaned word that has nothing but letters.
    """

    if not text:
        return text

    # Remove whitespace characters from the beginning and the end
    text = text.strip()

    for letter in text:
        if letter not in ase.LETTERS and letter != " ":
            text = text.replace(letter, "")

    return text
