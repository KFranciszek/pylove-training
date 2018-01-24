import requests

save_result = requests.post(
    'http://localhost:5000/save',
    json={'value': 'witam'}
)
print(save_result.text)

read_result = requests.get('http://localhost:5000/read')
print(read_result.text)