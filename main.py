import roman


def decimal_to_roman(dec_num):
    numerals = {
        1: 'I',
        4: 'IV',
        5: 'V',
        9: 'IX',
        10: 'X',
        40: 'XL',
        50: 'L',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        900: 'CM',
        1000: 'M'
    }

    r_num = '' if dec_num != 0 else 'N'

    while dec_num != 0:

        for i, numeral in enumerate([numeral for numeral in numerals.keys()][::-1]):
            if dec_num - numeral >= 0:
                r_num += numerals[numeral]
                dec_num -= numeral
                break

    return r_num


for i in range(1000):
    my = decimal_to_roman(i)
    truth = roman.toRoman(i)
    print(my == truth, i, my, truth)