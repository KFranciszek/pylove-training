import requests
resp = requests.get('http://py.net/status')
print(resp.json())
resp = requests.post(
    'http://py.net/status/set',
    json = {
        "status": "Nowy status"
    }
)
print(resp.json())
resp = requests.get('http://py.net/status')
print(resp.json())