import re


def pattern_sub(text: str, replacements: dict) -> str:
    """An alternative to "str".replace

    This function replaces multiple strings in a text using regex instead
    of looping of replacements.

    Args:
        text (str): The text we need to replace parts (or all) of it.
        replacements (dict): A map of all substrings and their replacements.

    Returns:
        str: The final text with replacements.
    """
    # use these three lines to do the replacement
    replacements = dict((re.escape(k), v) for k, v in replacements.items())

    pattern = re.compile("|".join(replacements.keys()))
    return pattern.sub(lambda m: replacements[re.escape(m.group(0))], text)
