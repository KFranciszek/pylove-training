import requests
resp = requests.post(
    'http://py.net/register',
    json = {
        "name": "JAnholcer",
        "password": "123456"
    }
)
print(resp.json())