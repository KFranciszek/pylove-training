import requests
resp = requests.post(
    "http://py.net/auth",
    json = {
        "name": "JAnholcer",
        "password": "123456"
    }
)
print(resp.json())