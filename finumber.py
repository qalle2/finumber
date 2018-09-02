import math
import sys

DIGITS = {
    0: "nolla",
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

# http://fi.wikipedia.org/wiki/Suurten_lukujen_nimet
# in nominative and partitive
# comment out keys you don't want to use
POWERS_OF_TEN = {
      1: ("kymmenen", "kymment\u00e4"),
      2: ("sata", "sataa"),
      3: ("tuhat", "tuhatta"),
      6: ("miljoona", "miljoonaa"),
      9: ("miljardi", "miljardia"),
     12: ("biljoona", "biljoonaa"),
     #15: ("biljardi", "biljardia"),  # rarely used
     18: ("triljoona", "triljoonaa"),
     #21: ("triljardi", "triljardia"),  # rarely used
     24: ("kvadriljoona", "kvadriljoonaa"),
     #27: ("kvadriljardi", "kvadriljardia"),  # rarely used
     30: ("kvintiljoona", "kvintiljoonaa"),
     36: ("sekstiljoona", "sekstiljoonaa"),
     42: ("septiljoona", "septiljoonaa"),
     48: ("oktiljoona", "oktiljoonaa"),
     54: ("noviljoona", "noviljoonaa"),  # or "noniljoona"
     60: ("dekiljoona", "dekiljoonaa"),
     66: ("undekiljoona", "undekiljoonaa"),
     72: ("duodekiljoona", "duodekiljoonaa"),
     78: ("tredekiljoona", "tredekiljoonaa"),
     84: ("kvattuordekiljoona", "kvattuordekiljoonaa"),
     90: ("kvindekiljoona", "kvindekiljoonaa"),
     96: ("sedekiljoona", "sedekiljoonaa"),
    102: ("septendekiljoona", "septendekiljoonaa"),
    108: ("duodevigintiljoona", "duodevigintiljoonaa"),
    114: ("undevigintiljoona", "undevigintiljoonaa"),
    120: ("vigintiljoona", "vigintiljoonaa"),
}

# " " = standard orthography
LEVEL1_SEPARATOR = " "

# "" = standard orthography, "\u00b7" = middle dot
LEVEL2_SEPARATOR = "\u00b7"

HELP_TEXT = """\
Prints a number in Finnish.
Argument: an integer between -10**126 and 10**126, exclusive.
You can use spaces or underscores ("_") as thousands separators.
Note: the middle dots ("\u00b7") are not part of the standard orthography.\
"""

def _less_than_10(n):
    if n == 0:
        return ""
    return DIGITS[n]

def _power_of_10(multiple, exponent):
    parts = []
    if multiple > 1:
        parts.append(DIGITS[multiple])
    if multiple and exponent:
        parts.append(POWERS_OF_TEN[exponent][0 if multiple == 1 else 1])
    return LEVEL2_SEPARATOR.join(parts)

def _less_than_100(n):
    (tens, ones) = divmod(n, 10)
    if tens == 1 and ones:
        parts = [DIGITS[ones], "toista"]
    else:
        parts = []
        if tens:
            parts.append(_power_of_10(tens, 1))
        if ones:
            parts.append(_less_than_10(ones))
    return LEVEL2_SEPARATOR.join(parts)

def _less_than_1000(n):
    (hundreds, ones) = divmod(n, 100)
    parts = []
    if hundreds:
        parts.append(_power_of_10(hundreds, 2))
    if ones:
        parts.append(_less_than_100(ones))
    return LEVEL2_SEPARATOR.join(parts)

def _power_of_1000(multiple, exponent):
    parts = []
    if multiple > 1 or exponent == 0:
        parts.append(_less_than_1000(multiple))
    if multiple and exponent:
        parts.append(POWERS_OF_TEN[exponent*3][0 if multiple == 1 else 1])
    separator = LEVEL1_SEPARATOR if exponent > 1 else LEVEL2_SEPARATOR
    return separator.join(parts)

def _less_than_1e6(n):
    (thousands, ones) = divmod(n, 1000)
    parts = []
    if thousands:
        parts.append(_power_of_1000(thousands, 1))
    if ones:
        parts.append(_less_than_1000(ones))
    return LEVEL1_SEPARATOR.join(parts)

def _power_of_1e6(multiple, exponent):
    parts = []
    if exponent * 6 + 3 in POWERS_OF_TEN:
        (thousands, ones) = divmod(multiple, 1000)
        if thousands:
            parts.append(_power_of_1000(thousands, exponent * 2 + 1))
        if ones:
            parts.append(_power_of_1000(ones, exponent * 2))
    else:
        if multiple > 1 or exponent == 0:
            parts.append(_less_than_1e6(multiple))
        if multiple and exponent:
            parts.append(POWERS_OF_TEN[exponent*6][0 if multiple == 1 else 1])
    return LEVEL1_SEPARATOR.join(parts)

def _positive_integer(n):
    # split to powers of million in reverse order
    powers = []
    while n:
        (n, remainder) = divmod(n, 10**6)
        powers.append(remainder)
    # format each nonzero power of million
    powers = [
        _power_of_1e6(power, i)
        for (i, power) in enumerate(powers)
        if power
    ]
    # return in correct order
    return LEVEL1_SEPARATOR.join(reversed(powers))

def Finnish_integer(n):
    parts = []
    if n < 0:
        parts.append("miinus")
    if n == 0:
        parts.append(DIGITS[0])
    else:
        parts.append(_positive_integer(abs(n)))
    return LEVEL1_SEPARATOR.join(parts)

def main():
    if len(sys.argv) != 2:
        exit(HELP_TEXT)

    n = sys.argv[1].replace(" ", "")
    try:
        n = int(n, 10)
    except ValueError:
        exit("Error: not an integer.")
    if abs(n) >= 10 ** (max(POWERS_OF_TEN) + 6):
        exit("Error: the number is too small or too large.")

    print(Finnish_integer(n))

assert Finnish_integer(-1).replace(LEVEL2_SEPARATOR, "") == "miinus yksi"
assert Finnish_integer(0).replace(LEVEL2_SEPARATOR, "") == "nolla"

assert Finnish_integer(1).replace(LEVEL2_SEPARATOR, "") == "yksi"
assert Finnish_integer(2).replace(LEVEL2_SEPARATOR, "") == "kaksi"
assert Finnish_integer(9).replace(LEVEL2_SEPARATOR, "") == "yhdeks\u00e4n"

assert Finnish_integer(10).replace(LEVEL2_SEPARATOR, "") == "kymmenen"
assert Finnish_integer(11).replace(LEVEL2_SEPARATOR, "") == "yksitoista"
assert Finnish_integer(12).replace(LEVEL2_SEPARATOR, "") == "kaksitoista"
assert Finnish_integer(19).replace(LEVEL2_SEPARATOR, "") == "yhdeks\u00e4ntoista"
assert Finnish_integer(20).replace(LEVEL2_SEPARATOR, "") == "kaksikymment\u00e4"
assert Finnish_integer(21).replace(LEVEL2_SEPARATOR, "") == "kaksikymment\u00e4yksi"
assert Finnish_integer(29).replace(LEVEL2_SEPARATOR, "") == "kaksikymment\u00e4yhdeks\u00e4n"
assert Finnish_integer(99).replace(LEVEL2_SEPARATOR, "") == "yhdeks\u00e4nkymment\u00e4yhdeks\u00e4n"

assert Finnish_integer(100).replace(LEVEL2_SEPARATOR, "") == "sata"
assert Finnish_integer(101).replace(LEVEL2_SEPARATOR, "") == "satayksi"
assert Finnish_integer(102).replace(LEVEL2_SEPARATOR, "") == "satakaksi"
assert Finnish_integer(199).replace(LEVEL2_SEPARATOR, "") == "satayhdeks\u00e4nkymment\u00e4yhdeks\u00e4n"
assert Finnish_integer(200).replace(LEVEL2_SEPARATOR, "") == "kaksisataa"
assert Finnish_integer(201).replace(LEVEL2_SEPARATOR, "") == "kaksisataayksi"
assert Finnish_integer(999).replace(LEVEL2_SEPARATOR, "") == "yhdeks\u00e4nsataayhdeks\u00e4nkymment\u00e4yhdeks\u00e4n"

assert Finnish_integer(1_000).replace(LEVEL2_SEPARATOR, "") == "tuhat"
assert Finnish_integer(1_001).replace(LEVEL2_SEPARATOR, "") == "tuhat yksi"
assert Finnish_integer(1_002).replace(LEVEL2_SEPARATOR, "") == "tuhat kaksi"
assert Finnish_integer(1_999).replace(LEVEL2_SEPARATOR, "") == "tuhat yhdeks\u00e4nsataayhdeks\u00e4nkymment\u00e4yhdeks\u00e4n"
assert Finnish_integer(2_000).replace(LEVEL2_SEPARATOR, "") == "kaksituhatta"
assert Finnish_integer(2_001).replace(LEVEL2_SEPARATOR, "") == "kaksituhatta yksi"

assert Finnish_integer(1_000_000).replace(LEVEL2_SEPARATOR, "") == "miljoona"
assert Finnish_integer(1_000_001).replace(LEVEL2_SEPARATOR, "") == "miljoona yksi"
assert Finnish_integer(1_000_002).replace(LEVEL2_SEPARATOR, "") == "miljoona kaksi"
assert Finnish_integer(2_000_000).replace(LEVEL2_SEPARATOR, "") == "kaksi miljoonaa"
assert Finnish_integer(2_000_001).replace(LEVEL2_SEPARATOR, "") == "kaksi miljoonaa yksi"

assert Finnish_integer(1_000_000_000).replace(LEVEL2_SEPARATOR, "") == "miljardi"
assert Finnish_integer(1_000_000_001).replace(LEVEL2_SEPARATOR, "") == "miljardi yksi"
assert Finnish_integer(1_000_000_002).replace(LEVEL2_SEPARATOR, "") == "miljardi kaksi"
assert Finnish_integer(2_000_000_000).replace(LEVEL2_SEPARATOR, "") == "kaksi miljardia"
assert Finnish_integer(2_000_000_001).replace(LEVEL2_SEPARATOR, "") == "kaksi miljardia yksi"

assert Finnish_integer(1_000_000_000_000).replace(LEVEL2_SEPARATOR, "") == "biljoona"
assert Finnish_integer(1_000_000_000_001).replace(LEVEL2_SEPARATOR, "") == "biljoona yksi"
assert Finnish_integer(1_000_000_000_002).replace(LEVEL2_SEPARATOR, "") == "biljoona kaksi"
assert Finnish_integer(2_000_000_000_000).replace(LEVEL2_SEPARATOR, "") == "kaksi biljoonaa"
assert Finnish_integer(2_000_000_000_001).replace(LEVEL2_SEPARATOR, "") == "kaksi biljoonaa yksi"

assert Finnish_integer(10**15).replace(LEVEL2_SEPARATOR, "") in ("biljardi", "tuhat biljoonaa")
assert Finnish_integer(10**21).replace(LEVEL2_SEPARATOR, "") in ("triljardi", "tuhat triljoonaa")
assert Finnish_integer(10**27).replace(LEVEL2_SEPARATOR, "") in ("kvadriljardi", "tuhat kvadriljoonaa")

assert Finnish_integer(10**120).replace(LEVEL2_SEPARATOR, "") == "vigintiljoona"
assert Finnish_integer(10**123).replace(LEVEL2_SEPARATOR, "") == "tuhat vigintiljoonaa"

if __name__ == "__main__":
    main()
