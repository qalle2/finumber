"""Tests for finumber.py"""

import finumber

TESTS = {
    -1: "miinus yksi",

    0: "nolla",

    1: "yksi",
    2: "kaksi",
    9: "yhdeksän",

    10: "kymmenen",
    11: "yksitoista",
    12: "kaksitoista",
    19: "yhdeksäntoista",

    20: "kaksikymmentä",
    21: "kaksikymmentäyksi",
    22: "kaksikymmentäkaksi",
    29: "kaksikymmentäyhdeksän",
    99: "yhdeksänkymmentäyhdeksän",

    100: "sata",
    101: "satayksi",
    102: "satakaksi",
    110: "satakymmenen",
    111: "satayksitoista",
    120: "satakaksikymmentä",
    123: "satakaksikymmentäkolme",
    199: "satayhdeksänkymmentäyhdeksän",

    200: "kaksisataa",
    201: "kaksisataayksi",
    202: "kaksisataakaksi",
    210: "kaksisataakymmenen",
    211: "kaksisataayksitoista",
    234: "kaksisataakolmekymmentäneljä",
    999: "yhdeksänsataayhdeksänkymmentäyhdeksän",

    1000: "tuhat",
    1001: "tuhat yksi",
    1002: "tuhat kaksi",
    1010: "tuhat kymmenen",
    1011: "tuhat yksitoista",
    1100: "tuhat sata",
    1101: "tuhat satayksi",
    1110: "tuhat satakymmenen",
    1111: "tuhat satayksitoista",
    1234: "tuhat kaksisataakolmekymmentäneljä",
    1999: "tuhat yhdeksänsataayhdeksänkymmentäyhdeksän",

    2000: "kaksituhatta",
    2001: "kaksituhatta yksi",
    2003: "kaksituhatta kolme",
    2345: "kaksituhatta kolmesataaneljäkymmentäviisi",

    1_000_000: "miljoona",
    1_000_001: "miljoona yksi",
    1_000_002: "miljoona kaksi",
    1_200_000: "miljoona kaksisataatuhatta",
    2_000_000: "kaksi miljoonaa",
    2_000_001: "kaksi miljoonaa yksi",

    1_000_000_000: "miljardi",
    1_000_000_001: "miljardi yksi",
    1_000_000_002: "miljardi kaksi",
    1_001_000_000: "miljardi miljoona",
    1_002_000_000: "miljardi kaksi miljoonaa",
    2_000_000_000: "kaksi miljardia",
    2_000_000_001: "kaksi miljardia yksi",
    2_001_000_000: "kaksi miljardia miljoona",

    1_000_000_000_000: "biljoona",
    1_000_000_000_001: "biljoona yksi",
    1_000_000_000_002: "biljoona kaksi",
    1_001_000_000_000: "biljoona miljardi",
    2_000_000_000_000: "kaksi biljoonaa",
    2_000_000_000_001: "kaksi biljoonaa yksi",

    1_000_000_000_000_000: "tuhat biljoonaa",
    1_001_000_000_000_000: "tuhat yksi biljoonaa",

    2_000_003_004_005_006_007: "kaksi triljoonaa kolme biljoonaa neljä miljardia viisi miljoonaa kuusituhatta seitsemän",

    1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000: "vigintiljoona",
}

def main():
    for n in sorted(TESTS):
        result = finumber.Finnish_integer(n)
        correctResult = TESTS[n]
        if result != correctResult:
            print("Incorrect result for {:d}:".format(n))
            print('Expected: "{:s}"'.format(correctResult))
            print('Got     : "{:s}"'.format(result))
            exit(1)
    print("All tests passed.")

if __name__ == "__main__":
    main()
