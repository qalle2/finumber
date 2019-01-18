import sys

MINUS = "miinus"
ZERO = "nolla"

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

# in nominative and partitive
POWERS_OF_TEN = {
    1: ("kymmenen", "kymmentä"),
    2: ("sata", "sataa"),
}

# in nominative and partitive
POWERS_OF_THOUSAND = {
    1: ("tuhat", "tuhatta"),
    3: ("miljardi", "miljardia"),
}

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

def less_than_ten(n):
    """n: 1-9"""
    return DIGITS[n]

def power_of_ten(multiple, exponent):
    """multiple: 1-9, exponent: 1-2"""
    parts = []
    if multiple > 1:
        parts.append(less_than_ten(multiple))
    parts.append(POWERS_OF_TEN[exponent][0 if multiple == 1 else 1])
    return "".join(parts)

def less_than_thousand(n):
    """n: 1-999"""
    (tens, ones) = divmod(n, 10)
    (hundreds, tens) = divmod(tens, 10)
    parts = []
    if hundreds:
        parts.append(power_of_ten(hundreds, 2))
    if tens == 1 and ones:
        parts.append(less_than_ten(ones))
        parts.append("toista")
    else:
        if tens:
            parts.append(power_of_ten(tens, 1))
        if ones:
            parts.append(less_than_ten(ones))
    return "".join(parts)

def power_of_thousand(multiple, exponent):
    """multiple: 1...999, exponent: 1 or 3"""
    parts = []
    if multiple > 1:
        parts.append(less_than_thousand(multiple))
    parts.append(POWERS_OF_THOUSAND[exponent][0 if multiple == 1 else 1])
    return ("" if exponent == 1 else " ").join(parts)

def less_than_million(n):
    """n: 1-999_999"""
    (thousands, ones) = divmod(n, 1000)
    parts = []
    if thousands:
        parts.append(power_of_thousand(thousands, 1))
    if ones:
        parts.append(less_than_thousand(ones))
    return " ".join(parts)

def power_of_million(multiple, exponent):
    """multiple: 1...999_999, exponent: 1 or greater"""
    parts = []
    if multiple > 1:
        parts.append(less_than_million(multiple))
    parts.append(
        POWERS_OF_MILLION[exponent]
        + ("iljoona" if multiple == 1 else "iljoonaa")
    )
    return " ".join(parts)

def power_of_million_with_exceptions(multiple, exponent):
    """multiple: 1-999_999, exponent: 0 or greater"""
    parts = []
    if exponent == 1:
        (thousands, multiple) = divmod(multiple, 1000)
        if thousands:
            parts.append(power_of_thousand(thousands, 3))
    if multiple:
        if exponent:
            parts.append(power_of_million(multiple, exponent))
        else:
            parts.append(less_than_million(multiple))
    return " ".join(parts)

def Finnish_positive_integer(n):
    """Format a positive integer."""
    # split to powers of million (smallest first)
    powers = []
    while n:
        (n, remainder) = divmod(n, 10**6)
        powers.append(remainder)
    # format each nonzero power
    powers = [
        power_of_million_with_exceptions(multiple, exponent)
        for (exponent, multiple) in enumerate(powers)
        if multiple
    ]
    # return in correct order (largest first)
    return " ".join(reversed(powers))

def Finnish_integer(n):
    """Format a Finnish integer."""
    parts = []
    if n < 0:
        parts.append(MINUS)
    if n == 0:
        parts.append(ZERO)
    else:
        parts.append(Finnish_positive_integer(abs(n)))
    return " ".join(parts)

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
