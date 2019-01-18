import sys

# less than nothing
MINUS = "miinus"

# nothing
ZERO = "nolla"

# positive integers smaller than the radix
DIGITS = {
    1: "yksi",
    2: "kaksi",
    3: "kolme",
    4: "neljä",
    5: "viisi",
    6: "kuusi",
    7: "seitsemän",
    8: "kahdeksan",
    9: "yhdeksän",
}

# for the irregular numbers 11-19
SECOND_TEN = "toista"

# small powers of the radix (nominative/partitive)
POWERS_OF_TEN = {
    1: ("kymmenen", "kymmentä"),
    2: ("sata", "sataa"),
}

# small powers of thousand (nominative/partitive)
POWERS_OF_THOUSAND = {
    1: ("tuhat", "tuhatta"),
    3: ("miljardi", "miljardia"),
}

# prefixes for powers of million
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

# suffixes for powers of million (nominative/partitive)
POWERS_OF_MILLION_ENDINGS = ("iljoona", "iljoonaa")

def less_than_ten(n):
    """Format 1...9."""

    return DIGITS[n]

def power_of_ten(multiple, exponent):
    """Format multiple * 10**exponent.
    multiple: 1...9, exponent: 1...2"""

    parts = []
    if multiple > 1:
        parts.append(less_than_ten(multiple))
    parts.append(POWERS_OF_TEN[exponent][0 if multiple == 1 else 1])
    return "".join(parts)

def less_than_thousand(n):
    """Format 1...999."""

    (tens, ones) = divmod(n, 10)
    (hundreds, tens) = divmod(tens, 10)
    parts = []

    if hundreds:
        parts.append(power_of_ten(hundreds, 2))

    if tens == 1 and ones:
        parts.append(less_than_ten(ones))
        parts.append(SECOND_TEN)
    else:
        if tens:
            parts.append(power_of_ten(tens, 1))
        if ones:
            parts.append(less_than_ten(ones))

    return "".join(parts)

def power_of_thousand(multiple, exponent):
    """Format multiple * 1_000**exponent.
    multiple: 1...999, exponent: 1 or 3"""

    parts = []
    if multiple > 1:
        parts.append(less_than_thousand(multiple))
    parts.append(POWERS_OF_THOUSAND[exponent][0 if multiple == 1 else 1])
    separator = "" if exponent == 1 else " "

    return separator.join(parts)

def less_than_million(n):
    """Format 1...999_999."""

    (thousands, ones) = divmod(n, 1000)
    parts = []
    if thousands:
        parts.append(power_of_thousand(thousands, 1))
    if ones:
        parts.append(less_than_thousand(ones))

    return " ".join(parts)

def power_of_million(multiple, exponent):
    """Format multiple * 1_000_000**exponent.
    multiple: 1...999_999, exponent: 0 or greater"""

    parts = []

    # separate the 1_000_000_000s if necessary
    if exponent == 1:
        (thousands, multiple) = divmod(multiple, 1000)
        if thousands:
            parts.append(power_of_thousand(thousands, 3))

    if multiple:
        # format multiple
        if not exponent or multiple > 1:
            parts.append(less_than_million(multiple))

        # format power of million (prefix + suffix)
        if exponent:
            parts.append(
                POWERS_OF_MILLION[exponent]
                + POWERS_OF_MILLION_ENDINGS[int(multiple > 1)]
            )

    return " ".join(parts)

def positive_integer(n):
    """Format a positive integer."""

    # split to powers of million (smallest first)
    powers = []
    while n:
        (n, remainder) = divmod(n, 10**6)
        powers.append(remainder)

    # format each nonzero power
    powers = [
        power_of_million(multiple, exponent)
        for (exponent, multiple) in enumerate(powers)
        if multiple
    ]

    # return in correct order (largest first)
    return " ".join(reversed(powers))

def Finnish_integer(n):
    """Format a Finnish integer."""

    if n == 0:
        return ZERO

    return (MINUS + " " if n < 0 else "") + positive_integer(abs(n))

def main():
    if len(sys.argv) != 2:
        exit("Syntax error. See the readme file.")

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
