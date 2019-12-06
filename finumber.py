"""Print an integer in Finnish."""

import sys

def less_than_ten(n):
    """Format 1-9."""

    digits = (  # "one" to "nine"
        "yksi", "kaksi", "kolme", "neljä", "viisi", "kuusi", "seitsemän", "kahdeksan", "yhdeksän"
    )
    return digits[n-1]

def less_than_thousand(n):
    """Format 1-999."""

    (tens, ones) = divmod(n, 10)
    (hundreds, tens) = divmod(tens, 10)
    parts = []
    if hundreds:
        parts.append(less_than_ten(hundreds) + "sataa" if hundreds > 1 else "sata")
    if tens == 1:
        parts.append(less_than_ten(ones) + "toista" if ones else "kymmenen")
    else:
        if tens:
            parts.append(less_than_ten(tens) + "kymmentä")
        if ones:
            parts.append(less_than_ten(ones))
    return "".join(parts)

def less_than_million(n):
    """Format 1-999_999."""

    (thousands, ones) = divmod(n, 1000)
    parts = []
    if thousands > 1:
        parts.append(less_than_thousand(thousands) + "tuhatta")
    elif thousands == 1:
        parts.append("tuhat")
    if ones:
        parts.append(less_than_thousand(ones))
    return " ".join(parts)

def power_of_million(multiple, exponent):
    """Format multiple * 1_000_000**exponent.
    multiple: 1-999_999, exponent: 0-20"""

    # prefixes for 10 ** (6n)
    powersOfMillion = (
        "m",            #  1
        "b",            #  2
        "tr",           #  3
        "kvadr",        #  4
        "kvint",        #  5
        "sekst",        #  6
        "sept",         #  7
        "okt",          #  8
        "nov",          #  9 (alternatively "non")
        "dek",          # 10
        "undek",        # 11
        "duodek",       # 12
        "tredek",       # 13
        "kvattuordek",  # 14
        "kvindek",      # 15
        "sedek",        # 16
        "septendek",    # 17
        "duodevigint",  # 18
        "undevigint",   # 19
        "vigint",       # 20
    )

    if exponent == 0:
        return less_than_million(multiple)
    if exponent == 1:
        # 1_000_000 to 999_999_000_000 (here "billion" = 10 ** 9)
        (billions, millions) = divmod(multiple, 1000)
        parts = []
        if billions > 1:
            parts.append(less_than_thousand(billions) + " miljardia")
        elif billions == 1:
            parts.append("miljardi")
        if millions > 1:
            parts.append(less_than_million(millions) + " miljoonaa")
        elif millions == 1:
            parts.append("miljoona")
        return " ".join(parts)
    parts = []
    if multiple > 1:
        parts.append(less_than_million(multiple))
        parts.append(powersOfMillion[exponent-1] + "iljoonaa")
    else:
        parts.append(powersOfMillion[exponent-1] + "iljoona")
    return " ".join(parts)

def positive_integer(n):
    """Format a positive integer."""

    # split to powers of million (smallest first)
    powersOfMillion = []
    while n:
        (n, remainder) = divmod(n, 10**6)
        powersOfMillion.append(remainder)
    # format each nonzero power
    powersOfMillion = [
        power_of_million(multiple, exponent)
        for (exponent, multiple) in enumerate(powersOfMillion) if multiple
    ]
    # return in correct order (largest first)
    return " ".join(reversed(powersOfMillion))

def Finnish_integer(n):
    """Format a Finnish integer."""

    if n == 0:
        return "nolla"
    return ("miinus " if n < 0 else "") + positive_integer(abs(n))

def main():
    """The main function."""

    if sys.version_info[0] != 3:
        print("Warning: possibly incompatible Python version.", file=sys.stderr)

    if len(sys.argv) != 2:
        sys.exit("Invalid number of command line arguments.")

    n = sys.argv[1].replace(" ", "")
    try:
        n = int(n, 10)
    except ValueError:
        sys.exit("The command line argument is not an integer.")
    if abs(n) >= 10 ** 126:
        sys.exit("The number is too small or too large.")
    print(Finnish_integer(n))

if __name__ == "__main__":
    main()
