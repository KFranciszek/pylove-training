import json
with open("py1.2zd.json", "r") as file:
    data = json.load(file)
ships = []
for ship in data:
    ships.append([(int(ship["cost_in_credits"]) if ship["cost_in_credits"] != "unknown" else 0), ship["name"]])
ships.sort()
with open("ships", "w") as file:
    for ship in ships:
        file.write("{0} kosztuje {1} credits. \n".format(ship[1], ship[0]))
