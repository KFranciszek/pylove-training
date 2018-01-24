lista_zakupow = []
koszyk = []
zgodne = []
niezgodne = []
brakujace = []

for i in range(0,5):
    lista_zakupow.append(input('Co mąż ma kupić? '))

for j in range(0,5):
    koszyk.append(input('Kochanie, kupiłem: '))
    if koszyk[j] in lista_zakupow:
        zgodne.append(koszyk[j])
    else:
        niezgodne.append(koszyk[j])

for produkt in lista_zakupow:
    if produkt not in koszyk:
        brakujace.append(produkt)

print('Mężowi udało się kupić według zamówienia: ' + str(zgodne))
print('Poza tym mąż kupił jeszcze: ' + str(niezgodne))
print('Żonie zabraknie: ' + str(brakujace))