def valid_input(dane):
    if isinstance(dane,(float,int)):
        return dane
    if not isinstance(dane, str):
        return False
    dane = dane.replace(',','.')
    try:
        return float(dane)
    except ValueError:
        return False

def read_number(info):
    while True:
        a = input(info)
        number = valid_input(a)
        if number:
            return number
        print('Podaj poprawną liczbę: ')

def bmi(w,h):
    bmi = round(w / (h ** 2), 2)
    return bmi

cont = True
while cont:
    name = input('Podaj imię: ')
    valid_sex = False
    plec = ''
    while not valid_sex:
        plec = input('Podaj płeć K/M: ').upper()
        if plec == 'K' or plec == 'M':
            valid_sex = True
    waga = read_number('Podaj wagę (w kilogramach): ')
    wzrost = read_number('Podaj wzrost (w metrach): ')
    moje_bmi = bmi(waga, wzrost)
    print(name + ', Twoje BMI wynosi: ' + str(moje_bmi))
    if plec == 'K':
        if moje_bmi < 19:
            print('Masz niedowagę, idź coś zjeść!')
        elif moje_bmi <= 27:
            print('Waga w normie, idź coś zjeść!')
        elif moje_bmi <= 31:
            print('Masz nadwagę, ale przecież nadal możesz coś zjeść')
        else:
            print('Otyłość')
    else:
         if moje_bmi < 18.5:
             print('Masz niedowagę, idź coś zjeść!')
         elif moje_bmi <= 25:
             print('Waga w normie, idź coś zjeść!')
         elif moje_bmi <= 30:
             print('Masz nadwagę, ale przecież nadal możesz coś zjeść')
         else:
             print('Otyłość')
    odp = input('Czy policzyć BMI dla kolejnej osoby? (jeżeli tak, wpisz T): ')
    odp = odp.upper()
    if odp != 'T':
        cont = False
