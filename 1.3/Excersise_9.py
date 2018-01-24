import requests
starships = requests.get("https://swapi.co/api/starships").json()["results"]
falcon = list(filter(lambda ship: ship["name"] == "Millennium Falcon", starships))[0]
pilots = []
for pilot in falcon["pilots"]:
    pilots.append(requests.get(pilot).json())
for pilot in pilots:
    pilot["bmi"] = int(pilot["mass"]) / (int(pilot["height"]) / 100) ** 2
    print("{0} - BMI: {1}".format(pilot["name"], round(pilot["bmi"], 2)))
