file = open("py1.2")
data = file.readlines()
file.close()
persons = {}
for i, person in enumerate(data):
    data[i] = person[(person.find(". ") + 2):]
    data[i] = data[i].split(" has ")
    data[i][1] = data[i][1].split(" and is ")
    data[i][1][1] = data[i][1][1].split(" cm tall")
    persons[data[i][0]] = {"height": data[i][1][1][0],"eyes": data[i][1][0]}

print(persons)
