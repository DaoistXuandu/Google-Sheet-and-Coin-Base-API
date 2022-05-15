from __future__ import print_function
from distutils.command.clean import clean
from multiprocessing.sharedctypes import Value
from threading import current_thread
from zoneinfo import available_timezones
from googleapiclient.discovery import build
from google.oauth2 import service_account
import json, hmac, hashlib, time, requests
from requests.auth import AuthBase
from coinbase.wallet.client import Client

def update(data):
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

        previousValue = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, 
                range="sales!E9:F183").execute()
        
        values =  previousValue.get('values', [])
        
        format_data = []
        total_amount = 0.00
        for i in data :
                arr = []
                current = "$ " + str(i[0])
                total_amount += float(i[0])
                arr.append(current)
                format_data.append(arr)


        valueInput = format_data
        total_amount = [['$ ' + str(total_amount)]]

        request = sheet.values().update(spreadsheetId= SAMPLE_SPREADSHEET_ID, 
                range="sales!E9:F183", valueInputOption="USER_ENTERED", 
                body={"values" : valueInput}).execute()
        
        request = sheet.values().update(spreadsheetId= SAMPLE_SPREADSHEET_ID, 
                range="sales!C9:D183", valueInputOption="USER_ENTERED", 
                body={"values" : values}).execute()

        request = sheet.values().update(spreadsheetId= SAMPLE_SPREADSHEET_ID, 
                range="sales!C7:F7", valueInputOption="USER_ENTERED", 
                body={"values" : total_amount}).execute()


def getData() :
        client = Client('3AXCJXgp1uJQGLZo', 'esaEwW8321rVixmFesMvn0fHDiNZS1Sz')

        user = client.get_user("436cd689-375d-5446-93b7-18583489a74c")
        accounts = client.get_accounts(id=user["id"])

        value_arr = []
        for i in accounts["data"] :
                current_data = []
                current_data.append(i["native_balance"]["amount"])
                value_arr.append(current_data)

        # print(value_arr)
        return value_arr


if __name__ == '__main__' :
        update(getData())

