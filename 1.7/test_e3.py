import requests

# changed_pass = requests.post(
#     "http://localhost:5000/user/user1/set-password",
#     json={"password": "nowo dodany"}
# )
# print(changed_pass.text)

login_log = requests.get(
    "http://localhost:5000/user/user1/login",
    json={"password": "password1"}
)
print(login_log.text)