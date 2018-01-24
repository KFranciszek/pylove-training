import requests
episodes = requests.get("https://swapi.co/api/films/").json()["results"]
episode5 = next((episode for episode in episodes if episode["episode_id"] == 5))
for species in episode5["species"]:
    print(requests.get(species).json()["name"])
