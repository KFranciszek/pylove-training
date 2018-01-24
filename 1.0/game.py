from random import randint as ri


def read_number(info):
    while True:
        try:
            return abs(int(input(info)))
        except ValueError:
            print('Podaj poprawną liczbę!')


odp = True
print('Zagrajmy z grę!')
tryb = read_number('Do jakiej liczby mam losować? Maksymalnie 1000. Przy większej liczbie będziesz miał większą ilość prób. ')
if tryb > 500:
    proby_maks = 8
else:
    proby_maks = 5

print('Zgadnij jaką liczbę z zakresu od 1 do {} mam na myśli. Masz {} prób.'.format(tryb, proby_maks))

while odp:
    mistery_number = ri(1, tryb)
    print('Wylosowałem nową liczbę.')
    proby = 1
    sukces = False
    while proby <= proby_maks:
        user_try = read_number('Czekam na Twój strzał: ')
        if mistery_number == user_try:
            print('Brawo, zgadłeś w ' + str(proby) + ' próbie!')
            proby = proby_maks + 1
            sukces = True
        elif user_try < mistery_number:
            print('Moja liczba jest większa.')
        else:
            print('Moja liczba jest mniejsza.')
        proby += 1
    if not sukces:
        print('Nie udało się tym razem.')
    pyt = input('Czy chcesz zagrać jeszcze raz? T/N').upper()
    if pyt != 'T':
        print('Fajnie się grało, papa')
        odp = False
