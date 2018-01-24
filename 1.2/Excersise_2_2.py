file = open("py1.2")
data = file.readlines()
file.close()
persons = {}
for i, person in enumerate(data):
    data[i] = person[(person.find(". ")+2):]
    data[i] = data[i].split(" has ")
    data[i][1] = data[i][1].split(" and is ")
    data[i][1][1] = data[i][1][1].split(" cm tall")
    persons[data[i][0]] = {"height": data[i][1][1][0],"eyes": data[i][1][0]}
file = open("hero_200_plus","w")
file2 = open("hero_short","w")
for x in persons:
    if int(persons[x]["height"]) > 200:
        file.writelines("{} \n".format(x))
    else:
        file2.writelines("{} \n".format(x))
file.close()
file2.close()