normal_mappings = {
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


def processor(text: str, use_hamza: bool = False, use_tarkeeb: bool = False):
    total = len(text)
    count = 0
    skip = False

    for i, char in enumerate(text):
        if skip:
            skip = False
            continue

        if not use_hamza and char == "ء":
            continue

        if use_tarkeeb and not char.isspace() and i + 1 < total and text[i + 1] == "غ":
            count += 1000 * normal_mappings[char]
            skip = True
            continue

        count += normal_mappings.get(char, 0)

    return count
