import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests

# Google Sheets API authentication
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    'credentials.json', scope)
client = gspread.authorize(credentials)

# Landbot API credentials
landbot_api_key = 'YOUR_LANDBOT_API_KEY'
landbot_api_url = 'https://api.landbot.io/v1/customers/send-whatsapp'

# Google Sheet details
sheet_name = 'Sheet1'
column_to_monitor = 'A'  # The column where changes are monitored

# Previous data placeholder
previous_data = []

# Function to send message via Landbot API


def send_message(recipient, message):
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


# Retrieve data from Google Sheet
sheet = client.open(sheet_name).sheet1
# Convert column letter to index (1-based)
data = sheet.col_values(ord(column_to_monitor.lower()) - 96)

# Check for changes and send messages
for index, value in enumerate(data):
    if index >= len(previous_data) or value != previous_data[index]:
        recipient = value  # Assuming phone numbers are in column A
        message = "Hello! Your data has changed in the Google Sheet."
        send_message(recipient, message)

# Update previous_data with the current data for future comparisons
previous_data = data
