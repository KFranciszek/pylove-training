import requests
resp = requests.get("http://py.net/cat")
with open("cat4.jpg", "wb") as file:
    file.write(resp.content)