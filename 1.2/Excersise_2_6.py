import json
encoding = "utf-8"
with open("py1.2.json", "r", encoding = encoding) as file:
    data = json.load(file)
file_all = open("sw_all_heros", "w", encoding = encoding)
for person in data:
    gender = ""
    homeworld = ""
    if person["gender"] == "male":
        gender = "mężczyzną"
    elif person["gender"] == "female":
        gender = "kobietą"
    else:
        gender = "nieokreślonej płci"
    if person["homeworld"] == "unknown":
        homeworld = "Galaktyki far, far away"
    else:
        homeworld = person["homeworld"]
    file_all.write("{0} waży {1} kg jest {2} i pochodzi z {3}.".format(person["name"], person["mass"], gender, homeworld))
    file_all.write("\n")
file_all.close()
