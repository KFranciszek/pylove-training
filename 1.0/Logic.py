cont = True
while cont:
    imie = input('Podaj imię: ')
    valid_sex = False
    plec = ''
    while not valid_sex:
        plec = input('Podaj płeć K/M: ').upper()
        if plec == 'K' or plec == 'M':
            valid_sex = True
    waga = input('Podaj wagę (w kilogramach): ')
    wzrost = input('Podaj wzrost (w metrach): ')
    bmi = round(float(waga) / (float(wzrost) ** 2),2)
    if plec == 'K':
        print(imie + ', Twoje BMI wynosi: ' + str(bmi))
        if bmi < 19:
            print('Masz niedowagę, idź coś zjeść!')
        elif bmi <= 27:
            print('Waga w normie, idź coś zjeść!')
        elif bmi <= 31:
            print('Masz nadwagę, ale przecież nadal możesz coś zjeść')
        else:
            print('Otyłość')
    else:
        print('Twoje BMI wynosi: ' + str(bmi))
        if bmi < 18.5:
            print('Masz niedowagę, idź coś zjeść!')
        elif bmi <= 25:
            print('Waga w normie, idź coś zjeść!')
        elif bmi <= 30:
            print('Masz nadwagę, ale przecież nadal możesz coś zjeść')
        else:
            print('Otyłość')
    odp = input('Czy policzyć BMI dla kolejnej osoby? (jeżeli tak, wpisz T): ')
    odp = odp.upper()
    if odp != 'T':
        cont = False
