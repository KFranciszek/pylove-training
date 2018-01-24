def to_roman(number):
    romans = [
        [
            '',
            'C',
            'CC',
            'CCC',
            'CD',
            'D',
            'DC',
            'DCC',
            'DCCC',
            'CM'
        ],
        [
        '',
        'X',
        'XX',
        'XXX',
        'XL',
        'L',
        'LX',
        'LXX',
        'LXXX',
        'XC'
        ],
        [
            '',
            'I',
            'II',
            'III',
            'IV',
            'V',
            'VI',
            'VII',
            'VIII',
            'IX'
        ]
        ]
    number = list(str(number))
    while len(number) < 4:
        number.insert(0,0)
    number[0] = int(number[0]) * 'M'
    for i in range(1,4):
        number[i] = romans[i-1][int(number[i])]
    return ''.join(number)

print(to_roman(2253))
print(to_roman(123))
print(to_roman(1164))
print(to_roman(3338))
print(to_roman(1002))
print(to_roman(94))
print(to_roman(17))


