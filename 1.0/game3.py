def ugly(numb):
    if numb == 1:
        return True
    if numb % 2 == 0 or numb % 3 == 0 or numb % 5 == 0:
        return True
    else:
        return False

for num in range(50):
    if ugly(num):
        print('Liczba {} jest liczbą brzydką.'.format(num))
    else:
        print('Liczba {} nie jest liczbą brzydką.'.format(num))