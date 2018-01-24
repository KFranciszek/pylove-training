list_persons = [[],[],[]]

list_persons[0].append(input('Podaj imię 1 osoby: '))
list_persons[0].append(int(input('Podaj wiek 1 osoby: ')))
list_persons[1].append(input('Podaj imię 2 osoby: '))
list_persons[1].append(int(input('Podaj wiek 2 osoby: ')))
list_persons[2].append(input('Podaj imię 3 osoby: '))
list_persons[2].append(int(input('Podaj wiek 3 osoby: ')))

print(list_persons)
print([list_persons[0][0],list_persons[1][0],list_persons[2][0]])
print([list_persons[0][1],list_persons[1][1],list_persons[2][1]])
print(list_persons[0])
print(list_persons[1])
print(list_persons[2])