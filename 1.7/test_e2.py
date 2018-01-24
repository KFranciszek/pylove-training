import requests

save_result = requests.post(
    "http://localhost:5000/current_status",
    json={"status": "nowy status"}
)
print(save_result.text)

read_result = requests.get("http://localhost:5000/current_status")
print(read_result.text)