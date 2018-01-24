def roman(numb):
    if numb > 4999:
        return 'Expected value in range (0,4999)'

    roman_units = [
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
    roman_tens = [
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
    ]
    roman_hundrets = [
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
    ]
    roman_tousends = [
        '',
        'M',
        'MM',
        'MMM',
        'MMMM'
    ]

    number = list(str(numb))
    while len(number) < 4:
        number.insert(0,0)

    roman_number = []

    roman_number.append(roman_tousends[int(number[0])])
    roman_number.append(roman_hundrets[int(number[1])])
    roman_number.append(roman_tens[int(number[2])])
    roman_number.append(roman_units[int(number[3])])

    roman_number = ''.join(roman_number)
    return roman_number

for number in range(1,4500,87):
    print(str(number) + ' : ' + roman(number))