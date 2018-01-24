import math
r = float(input('Podaj długość promienia podstawy w cm: '))
h = float(input('Podaj wysokość stożka w cm: '))
pow_podst = math.pi * r ** 2
l = math.sqrt(h**2 + r**2)
pow_bocz = math.pi*r*l
volume = pow_podst * h / 3
print('Stożek ma podstawę o powierzchni ' + str(pow_podst) + ' cm2, jego powierzchnia boczna wynosi ' + str(pow_bocz)+' cm2, a jego objętość wynosi ' + str(volume) +' cm3.')
