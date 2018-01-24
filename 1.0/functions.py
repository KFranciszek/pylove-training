def moje_dzialanie(a,b,oper='dodawanie'):
    c = 0
    if oper == 'dodawanie':
        c = a + b
    elif oper == 'odejmowanie':
        c = a - b
    elif oper == 'mnozenie':
        c = a * b
    elif oper == 'dzielenie':
        c = a / b
    if c:
        print('Wynik ' + oper[:(len(oper)-1)] +'a liczb ' + str(a) + ' i ' + str(b) + ' wynosi: ' + str(c))
    else:
        print ('Nie znam tego działania ;-)')

moje_dzialanie(12,6)
moje_dzialanie(12,6,'dupa')
moje_dzialanie(12,6,'odejmowanie')
moje_dzialanie(12,6,'mnozenie')
moje_dzialanie(12,6,'dzielenie')