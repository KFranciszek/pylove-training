import requests
gungans = requests.get("https://swapi.co/api/species/?search=gungan").json()["results"][0]["people"]
for gungan in gungans:
    gun = requests.get(gungan + '?format=wookiee').json()
    print(gun["whrascwo"])
