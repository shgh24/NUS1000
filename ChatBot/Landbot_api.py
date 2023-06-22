# import gspread
# from oauth2client.service_account import ServiceAccountCredentials
import requests

import gspread
from google.oauth2 import service_account

# # Google Sheets API authentication
# scope = ['https://spreadsheets.google.com/feeds',
#          'https://www.googleapis.com/auth/drive']
# credentials = ServiceAccountCredentials.from_json_keyfile_name(
#     'credentials.json', scope)
# client = gspread.authorize(credentials)


scope = ['https://www.googleapis.com/auth/spreadsheets']
creds = service_account.Credentials.from_service_account_file(
    '/Users/cnladmin/Documents/GitHub/NUS1000/ChatBot/nus1000-compliance-check-ff85914ee1c6.json', scopes=scope)
client = gspread.authorize(creds)

print('stoped here')


# Landbot API credentials
landbot_api_key = '07e78931a663148cfb58e157535bc515e4933f6a'
landbot_api_url = 'https://api.landbot.io/v1/customers/send-whatsapp'

# https: // api.landbot.io/v1/channels /: channel_id/
# https: // api.landbot.io/v1/customers /: customer_id/send_text/


# Google Sheet details
sheet_name = 'Sheet1'
column_to_monitor = 'Oura'  # The column where changes are monitored

# Previous data placeholder
previous_data = []

# Function to send message via Landbot API

# recipient = +6582264058  # Assuming phone numbers are in column A
# message = "Hello! Your data has changed in the Google Sheet."


customer_id = "276350857"
message = "Hello"
api_token = landbot_api_key

url = f"https://api.landbot.io/v1/customers/{customer_id}/send_text/"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_token}"
}
data = {
    "message": message
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    print("Message sent successfully!")
else:
    print("Failed to send message. Status code:", response.status_code)


# send_message(recipient, message)
payload = {
    'phone_number': recipient,
    'message': message,
    'api_key': landbot_api_key
}
response = requests.post(landbot_api_url, json=payload)
if response.status_code == 200:
    print(f"Message sent successfully to {recipient}")
else:
    print(f"Failed to send message to {recipient}")

# def send_message(recipient, message):
#     payload = {
#         'phone_number': recipient,
#         'message': message,
#         'api_key': landbot_api_key
#     }
#     response = requests.post(landbot_api_url, json=payload)
#     if response.status_code == 200:
#         print(f"Message sent successfully to {recipient}")
#     else:
#         print(f"Failed to send message to {recipient}")


# send_message(recipient, message)


# Retrieve data from Google Sheet
# sheet = client.open(sheet_name).sheet1
# Convert column letter to index (1-based)
# data = sheet.col_values(ord(column_to_monitor.lower()) - 96)

# # Check for changes and send messages
# for index, value in enumerate(data):
#     if index >= len(previous_data) or value != previous_data[index]:
#         recipient = value  # Assuming phone numbers are in column A
#         message = "Hello! Your data has changed in the Google Sheet."
#         send_message(recipient, message)

# # Update previous_data with the current data for future comparisons
# previous_data = data
