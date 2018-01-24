import json
encoding = "iso-8859-1"
with open("py1.2.json", "r") as file:
    data = json.load(file)
file_wom = open("sw_women", "w", encoding = encoding)
file_men = open("sw_men", "w", encoding = encoding)
for person in data:
    if person["gender"] == "female":
        file_wom.write(person["name"])
        file_wom.write("\n")
    elif person["gender"] == "male":
        file_men.write(person["name"])
        file_men.write("\n")
file_wom.close()
file_men.close()
