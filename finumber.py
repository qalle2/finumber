import sys

DIGITS = {
    1: "yksi",
    2: "kaksi",
    3: "kolme",
    4: "nelj\u00e4",
    5: "viisi",
    6: "kuusi",
    7: "seitsem\u00e4n",
    8: "kahdeksan",
    9: "yhdeks\u00e4n",
}

# in nominative and partitive
POWERS_OF_TEN = {
    1: ("kymmenen", "kymment\u00e4"),
    2: ("sata", "sataa"),
}

# in nominative and partitive
POWERS_OF_THOUSAND = {
    1: ("tuhat", "tuhatta"),
    3: ("miljardi", "miljardia"),
}

# http://fi.wikipedia.org/wiki/Suurten_lukujen_nimet
# "-iljoona" (nominative) and "-iljoonaa" (partitive) will be added
POWERS_OF_MILLION = {
    1: "m",
    2: "b",
    3: "tr",
    4: "kvadr",
    5: "kvint",
    6: "sekst",
    7: "sept",
    8: "okt",
    9: "nov",  # or "non"
    10: "dek",
    11: "undek",
    12: "duodek",
    13: "tredek",
    14: "kvattuordek",
    15: "kvindek",
    16: "sedek",
    17: "septendek",
    18: "duodevigint",
    19: "undevigint",
    20: "vigint",
}

HELP_TEXT = """\
Prints a number in Finnish.
Argument: an integer between -10**126 and 10**126, exclusive.
You can use spaces or underscores ("_") as thousands separators.\
"""

def _less_than_ten(n: int) -> str:
    """n: 1-9"""
    return DIGITS[n]

def _power_of_ten(multiple: int, exponent: int) -> str:
    """multiple: 1-9, exponent: 1-2"""
    parts = []
    if multiple > 1:
        parts.append(_less_than_ten(multiple))
    parts.append(POWERS_OF_TEN[exponent][0 if multiple == 1 else 1])
    return "".join(parts)

def _less_than_thousand(n: int) -> str:
    """n: 1-999"""
    (tens, ones) = divmod(n, 10)
    (hundreds, tens) = divmod(tens, 10)
    parts = []
    if hundreds:
        parts.append(_power_of_ten(hundreds, 2))
    if tens == 1 and ones:
        parts.append(_less_than_ten(ones))
        parts.append("toista")
    else:
        if tens:
            parts.append(_power_of_ten(tens, 1))
        if ones:
            parts.append(_less_than_ten(ones))
    return "".join(parts)

def _power_of_thousand(multiple: int, exponent: int) -> str:
    """multiple: 1...999, exponent: 1 or 3"""
    parts = []
    if multiple > 1:
        parts.append(_less_than_thousand(multiple))
    parts.append(POWERS_OF_THOUSAND[exponent][0 if multiple == 1 else 1])
    return ("" if exponent == 1 else " ").join(parts)

def _less_than_million(n: int) -> str:
    """n: 1-999_999"""
    (thousands, ones) = divmod(n, 1000)
    parts = []
    if thousands:
        parts.append(_power_of_thousand(thousands, 1))
    if ones:
        parts.append(_less_than_thousand(ones))
    return " ".join(parts)

def _power_of_million(multiple: int, exponent: int) -> str:
    """multiple: 1...999_999, exponent: 1 or greater"""
    parts = []
    if multiple > 1:
        parts.append(_less_than_million(multiple))
    parts.append(
        POWERS_OF_MILLION[exponent]
        + ("iljoona" if multiple == 1 else "iljoonaa")
    )
    return " ".join(parts)

def _power_of_million_with_exceptions(multiple: int, exponent: int) -> str:
    """multiple: 1-999_999, exponent: 0 or greater"""
    parts = []
    if exponent == 1:
        (thousands, multiple) = divmod(multiple, 1000)
        if thousands:
            parts.append(_power_of_thousand(thousands, 3))
    if multiple:
        if exponent:
            parts.append(_power_of_million(multiple, exponent))
        else:
            parts.append(_less_than_million(multiple))
    return " ".join(parts)

def _Finnish_positive_integer(n: int) -> str:
    """Format a positive integer."""
    # split to powers of million (smallest first)
    powers = []
    while n:
        (n, remainder) = divmod(n, 10**6)
        powers.append(remainder)
    # format each nonzero power
    powers = [
        _power_of_million_with_exceptions(multiple, exponent)
        for (exponent, multiple) in enumerate(powers)
        if multiple
    ]
    # return in correct order (largest first)
    return " ".join(reversed(powers))

def Finnish_integer(n: int) -> str:
    """Format a Finnish integer."""
    parts = []
    if n < 0:
        parts.append("miinus")
    if n == 0:
        parts.append("nolla")
    else:
        parts.append(_Finnish_positive_integer(abs(n)))
    return " ".join(parts)

def main():
    if len(sys.argv) != 2:
        exit(HELP_TEXT)

    n = sys.argv[1].replace(" ", "")
    try:
        n = int(n, 10)
    except ValueError:
        exit("Error: not an integer.")
    if abs(n) >= 10 ** (max(POWERS_OF_MILLION) * 6 + 6):
        exit("Error: the number is too small or too large.")

    print(Finnish_integer(n))

if __name__ == "__main__":
    main()
