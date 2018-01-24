file = open("py1.2")
data = file.readlines()  # czyta wszystkie linie
file.close()
persons = {}

for i, person in enumerate(data):
    data[i] = person[(person.find(". ")+2):]
    data[i] = data[i].split(" has ")
    data[i][1] = data[i][1].split(" and is ")
    data[i][1][1] = data[i][1][1].split(" cm tall")
    persons[data[i][0]] = {"height": data[i][1][1][0],"eyes": data[i][1][0]}

persons_by_color = {
    "blue":{"heights":[],"avr": 0},
    "brown":{"heights":[],"avr": 0},
    "black":{"heights":[],"avr": 0},
    "yellow":{"heights":[],"avr": 0},
    "pink":{"heights":[],"avr": 0},
    "unknown":{"heights":[],"avr": 0},
    "hazel":{"heights":[],"avr": 0},
    "orange":{"heights":[],"avr": 0},
    "red":{"heights":[],"avr": 0},
    "red, blue":{"heights":[],"avr": 0}
}
colors_pl = {
    "blue": "niebieskie",
    "brown": "brązowe",
    "black": "czarne",
    "yellow": "żółte",
    "pink": "różowe",
    "unknown": "nieznane",
    "hazel": "piwne",
    "orange": "pomarańczowe",
    "red": "czerwone",
    "red, blue": "czerwone, niebieskie"
}
file = open("pers_by_color_pl.txt","w")
for color in persons_by_color:
    for x in persons:
        if persons[x]["eyes"] == color:
            persons_by_color[color]["heights"].append(int(persons[x]["height"]))
    total_h = 0
    for i in range(0,len(persons_by_color[color]["heights"])):
        total_h += persons_by_color[color]["heights"][i]
    persons_by_color[color]["avr"] = total_h / len(persons_by_color[color]["heights"])
    file.writelines("Średni wzrost osób, których oczy są {0} wynosi {1} cm.\n".format(colors_pl[color], round(persons_by_color[color]["avr"],2)))
file.close()