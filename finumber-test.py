"""Tests for finumber.py"""

import sys
import finumber

TESTS = {
    -1_000_000_000_000_000_000: "miinus triljoona",

    -2: "miinus kaksi",
    -1: "miinus yksi",

    0: "nolla",
    1: "yksi",
    2: "kaksi",
    3: "kolme",
    4: "neljä",
    5: "viisi",
    6: "kuusi",
    7: "seitsemän",
    8: "kahdeksan",
    9: "yhdeksän",

    10: "kymmenen",
    11: "yksitoista",
    12: "kaksitoista",
    19: "yhdeksäntoista",
    20: "kaksikymmentä",
    21: "kaksikymmentäyksi",
    22: "kaksikymmentäkaksi",
    29: "kaksikymmentäyhdeksän",
    90: "yhdeksänkymmentä",
    91: "yhdeksänkymmentäyksi",
    92: "yhdeksänkymmentäkaksi",
    99: "yhdeksänkymmentäyhdeksän",

    100: "sata",
    101: "satayksi",
    102: "satakaksi",
    109: "satayhdeksän",
    110: "satakymmenen",
    111: "satayksitoista",
    112: "satakaksitoista",
    120: "satakaksikymmentä",
    121: "satakaksikymmentäyksi",
    122: "satakaksikymmentäkaksi",
    190: "satayhdeksänkymmentä",
    191: "satayhdeksänkymmentäyksi",
    192: "satayhdeksänkymmentäkaksi",
    199: "satayhdeksänkymmentäyhdeksän",
    200: "kaksisataa",
    201: "kaksisataayksi",
    202: "kaksisataakaksi",
    210: "kaksisataakymmenen",
    211: "kaksisataayksitoista",
    212: "kaksisataakaksitoista",
    220: "kaksisataakaksikymmentä",
    290: "kaksisataayhdeksänkymmentä",
    299: "kaksisataayhdeksänkymmentäyhdeksän",
    900: "yhdeksänsataa",
    999: "yhdeksänsataayhdeksänkymmentäyhdeksän",

    1_000: "tuhat",
    1_001: "tuhat yksi",
    1_002: "tuhat kaksi",
    1_010: "tuhat kymmenen",
    1_011: "tuhat yksitoista",
    1_100: "tuhat sata",
    1_101: "tuhat satayksi",
    1_110: "tuhat satakymmenen",
    1_111: "tuhat satayksitoista",
    1_234: "tuhat kaksisataakolmekymmentäneljä",
    1_999: "tuhat yhdeksänsataayhdeksänkymmentäyhdeksän",
    2_000: "kaksituhatta",
    2_001: "kaksituhatta yksi",
    2_002: "kaksituhatta kaksi",
    2_010: "kaksituhatta kymmenen",
    2_100: "kaksituhatta sata",
    2_101: "kaksituhatta satayksi",
    2_345: "kaksituhatta kolmesataaneljäkymmentäviisi",

    10_000: "kymmenentuhatta",
    10_001: "kymmenentuhatta yksi",
    20_000: "kaksikymmentätuhatta",
    65_535: "kuusikymmentäviisituhatta viisisataakolmekymmentäviisi",

    100_000: "satatuhatta",
    100_001: "satatuhatta yksi",
    200_000: "kaksisataatuhatta",

    1_000_000: "miljoona",
    1_000_001: "miljoona yksi",
    1_000_002: "miljoona kaksi",
    1_001_000: "miljoona tuhat",
    1_001_001: "miljoona tuhat yksi",
    1_200_000: "miljoona kaksisataatuhatta",
    2_000_000: "kaksi miljoonaa",
    2_000_001: "kaksi miljoonaa yksi",
    2_003_004: "kaksi miljoonaa kolmetuhatta neljä",

    10_000_000: "kymmenen miljoonaa",
    10_000_001: "kymmenen miljoonaa yksi",
    20_000_000: "kaksikymmentä miljoonaa",

    100_000_000: "sata miljoonaa",
    100_000_001: "sata miljoonaa yksi",
    200_000_000: "kaksisataa miljoonaa",

    1_000_000_000: "miljardi",
    1_000_000_001: "miljardi yksi",
    1_000_000_002: "miljardi kaksi",
    1_000_001_000: "miljardi tuhat",
    1_000_001_001: "miljardi tuhat yksi",
    1_001_000_000: "miljardi miljoona",
    1_001_000_001: "miljardi miljoona yksi",
    1_001_001_000: "miljardi miljoona tuhat",
    1_001_001_001: "miljardi miljoona tuhat yksi",
    1_002_000_000: "miljardi kaksi miljoonaa",
    2_000_000_000: "kaksi miljardia",
    2_000_000_001: "kaksi miljardia yksi",
    2_001_000_000: "kaksi miljardia miljoona",
    2_003_004_005: "kaksi miljardia kolme miljoonaa neljätuhatta viisi",
    4_294_967_295: "neljä miljardia kaksisataayhdeksänkymmentäneljä miljoonaa yhdeksänsataakuusikymmentäseitsemäntuhatta kaksisataayhdeksänkymmentäviisi",

    10_000_000_000: "kymmenen miljardia",
    10_000_000_001: "kymmenen miljardia yksi",
    11_000_000_000: "yksitoista miljardia",
    20_000_000_000: "kaksikymmentä miljardia",

    100_000_000_000: "sata miljardia",
    100_000_000_001: "sata miljardia yksi",
    200_000_000_000: "kaksisataa miljardia",

    1_000_000_000_000: "biljoona",
    1_000_000_000_001: "biljoona yksi",
    1_000_000_000_002: "biljoona kaksi",
    1_000_000_001_000: "biljoona tuhat",
    1_000_000_001_001: "biljoona tuhat yksi",
    1_000_001_000_000: "biljoona miljoona",
    1_000_001_000_001: "biljoona miljoona yksi",
    1_000_001_001_000: "biljoona miljoona tuhat",
    1_000_001_001_001: "biljoona miljoona tuhat yksi",
    1_001_000_000_000: "biljoona miljardi",
    1_001_000_000_001: "biljoona miljardi yksi",
    1_001_000_001_000: "biljoona miljardi tuhat",
    1_001_000_001_001: "biljoona miljardi tuhat yksi",
    1_001_001_000_000: "biljoona miljardi miljoona",
    1_001_001_000_001: "biljoona miljardi miljoona yksi",
    1_001_001_001_000: "biljoona miljardi miljoona tuhat",
    1_001_001_001_001: "biljoona miljardi miljoona tuhat yksi",
    2_000_000_000_000: "kaksi biljoonaa",
    2_000_000_000_001: "kaksi biljoonaa yksi",
    2_003_004_005_006: "kaksi biljoonaa kolme miljardia neljä miljoonaa viisituhatta kuusi",

    10_000_000_000_000: "kymmenen biljoonaa",
    10_000_000_000_001: "kymmenen biljoonaa yksi",
    11_000_000_000_000: "yksitoista biljoonaa",
    20_000_000_000_000: "kaksikymmentä biljoonaa",

    100_000_000_000_000: "sata biljoonaa",
    100_000_000_000_001: "sata biljoonaa yksi",
    200_000_000_000_000: "kaksisataa biljoonaa",

    1_000_000_000_000_000: "tuhat biljoonaa",
    1_000_000_000_000_001: "tuhat biljoonaa yksi",
    1_001_000_000_000_000: "tuhat yksi biljoonaa",
    2_000_000_000_000_000: "kaksituhatta biljoonaa",

    10_000_000_000_000_000: "kymmenentuhatta biljoonaa",
    10_000_000_000_000_001: "kymmenentuhatta biljoonaa yksi",
    20_000_000_000_000_000: "kaksikymmentätuhatta biljoonaa",

    100_000_000_000_000_000: "satatuhatta biljoonaa",
    100_000_000_000_000_001: "satatuhatta biljoonaa yksi",
    123_456_000_000_000_000: "satakaksikymmentäkolmetuhatta neljäsataaviisikymmentäkuusi biljoonaa",
    200_000_000_000_000_000: "kaksisataatuhatta biljoonaa",

    1_000_000_000_000_000_000: "triljoona",
    1_000_000_000_000_000_001: "triljoona yksi",
    1_000_001_001_001_001_001: "triljoona biljoona miljardi miljoona tuhat yksi",
    2_000_000_000_000_000_000: "kaksi triljoonaa",
    2_000_003_004_005_006_007: "kaksi triljoonaa kolme biljoonaa neljä miljardia viisi miljoonaa kuusituhatta seitsemän",

    1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000: "vigintiljoona",
    1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_001: "vigintiljoona yksi",
    2_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000: "kaksi vigintiljoonaa",
}

def main():
    """The main function."""

    for n in sorted(TESTS):
        result = finumber.Finnish_integer(n)
        correctResult = TESTS[n]
        if result != correctResult:
            print("Incorrect result for {:d}:".format(n), file=sys.stderr)
            print('Expected: "{:s}"'.format(correctResult), file=sys.stderr)
            print('Got     : "{:s}"'.format(result), file=sys.stderr)
            sys.exit(1)
    print("All tests passed.")

if __name__ == "__main__":
    main()
