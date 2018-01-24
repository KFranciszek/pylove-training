import requests
resp1 = requests.post(
    "http://py.net/auth",
    json = {
        "name": "JAnholcer",
        "password": "123456"
    }
)
resp2 = requests.post(
    "http://py.net/user_status/set",
    json = {
        "api_key" : resp1.json()["api_key"],
        "status" : "Brand new status"
    }
)
resp3 = requests.get("http://py.net/user_status")
print(resp1.json())
print(resp2.json())
print(resp3.json())
print(resp3.json()["WeronikaF"])
