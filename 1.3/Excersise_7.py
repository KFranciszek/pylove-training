import requests
import pprint
star_wars = requests.get("https://swapi.co/api/planets")
planets = star_wars.json()["results"]
while star_wars.json()["next"]:
    star_wars = requests.get(star_wars.json()["next"])
    planets += star_wars.json()["results"]
residents_api = next((planet for planet in planets if planet["name"] == "Tatooine"))["residents"]
residents = []
for resident in residents_api:
    resp = requests.get(resident)
    residents.append(resp.json())
pprint.pprint(residents)