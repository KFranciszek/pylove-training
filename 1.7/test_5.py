import requests

add_users = requests.post(
    "http://localhost:5000/users/add",
    json = {"imie": "Adam", "wiek": "15", "plec": "m"}
)

print(add_users.text)