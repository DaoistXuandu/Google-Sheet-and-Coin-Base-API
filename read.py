from __future__ import print_function
from googleapiclient.discovery import build
from google.oauth2 import service_account

SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)


# The ID 
SAMPLE_SPREADSHEET_ID = '1shmWZ_C695lhcJs6K21HP59bLmjXYn53XBztYHygGNg'

service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
valueInput = [["36509"]]
request = service.spreadsheets().values().update(spreadsheetId= SAMPLE_SPREADSHEET_ID, 
        range="sales!C7:D7", valueInputOption="USER_ENTERED", body={"values" : valueInput}).execute()

print(values)

