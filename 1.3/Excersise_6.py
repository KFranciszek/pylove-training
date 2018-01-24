import requests
resp1 = requests.get("http://py.net/query_string?arg1=dupa")
resp2 = requests.get("http://py.net/query_string")
print(resp1.json())
print(resp2.json())