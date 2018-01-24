import random


def read_number(info):
    while True:
        try:
            return abs(int(input(info)))
        except ValueError:
            print('Podaj poprawną liczbę!')


zwierzeta = ['pies',
             'kot',
             'tygrys',
             'koza',
             'krowa',
             'szczur',
             'pyton',
             'owca',
             'kaczka',
             'humbak',
             'aligator',
             'biedronka',
             'albatros',
             'antylopa',
             'zebra']
meble = ['kanapa',
         'lodówka',
         'krzesło',
         'lustro',
         'fotel',
         'wanna',
         'biurko',
         'telewizor',
         'komputer']
owoce = ['jabłko',
         'ananas',
         'banan',
         'papaja',
         'mango',
         'arbuz',
         'marchew',
         'dynia',
         'truskawka',
         'cytryna',
         'jagoda',
         'pietruszka',
         'pomidor',
         'awokado',
         'melon',
         'seler']


odp = False
liczba_prob = 0

while True:
    category = read_number('Wybierz kategorię: 1 - zwierzęta, 2 - elementy wyposażenia domu, 3 - owoce i warzywa: ')
    if category in [1, 2, 3]:
        break
    else:
        print('Podaj poprawną liczbę!')

if category == 1:
    category = 'zwierzęta'
    haslo = random.choice(zwierzeta)
elif category == 2:
    category = 'elementy wyposażenia domu'
    haslo = random.choice(meble)
else:
    category = 'owoce i warzywa'
    haslo = random.choice(owoce)

print('Losuję wyraz z kategorii ' + category + '.')
strzal = list(len(haslo)*'*')
print('Hasło: ' + ''.join(strzal))

while not odp:
    user_guess = input('Podaj literkę lub odgadnij hasło. (Wpisz EXIT żeby zakończyć): ')
    if user_guess.upper() == 'EXIT':
        print('Podjąłeś {0} prób i zrezygnowałeś. Prawidłowe hasło to: {1}. Do zobaczenia.'.format(liczba_prob, haslo))
        odp = False
        break
    else:
        liczba_prob += 1
        if len(user_guess) > 1:
            if user_guess == haslo:
                print('Brawo, odgadłeś hasło {} w {} próbie!!!'.format(haslo, liczba_prob))
                odp = False
                break
            else:
                print('To nie jest prawidłowe hasło...')
        else:
            sukces = False
            for i in range(len(haslo)):
                if haslo[i] == user_guess:
                    sukces = True
                    strzal[i] = user_guess
            if sukces:
                print('Trafiłeś!!')
            else:
                print('Próbuj dalej!!')
            print('Hasło: ' + ''.join(strzal))
            try:
                strzal.index('*')
            except ValueError:
                print('Brawo, odgadłeś hasło {} w {} próbie!!!'.format(haslo, liczba_prob))
                odp = False
                break
