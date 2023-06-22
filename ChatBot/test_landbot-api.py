

import requests

landbot_api_key = "07e78931a663148cfb58e157535bc515e4933f6a"

response = requests.get("https://api.landbot.io/")


customer_id = "276350857"
message = "Hello"
# api_token = landbot_api_key

agent_token = landbot_api_key


channel_id = "1625018"
url = f"https://api.landbot.io/v1/channels/{channel_id}/"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {agent_token}"
}

response = requests.get(url, headers=headers)
headers = {"HTTP_HOST": "MyVeryOwnHost"}

url = f"https://api.landbot.io/v1/customers/{customer_id}/send_text/"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Token {agent_token}"
}
data = {
    "message": message
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    print("Message sent successfully!")
else:
    print("Failed to send message. Status code:", response.status_code)

print("done")
