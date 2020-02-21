# coding: utf-8
from pprint import pprint
import httplib2 
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials	

CREDENTIALS_FILE = 'myJson.json' 

credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'])

httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth) 

spreadsheetId = 'token_Excel'

ranges = ["A1:A19"]
          
results = service.spreadsheets().values().batchUpdate(spreadsheetId = spreadsheetId, body = {
    "valueInputOption": "USER_ENTERED",
    "data": [
        {"range": "B2:D5",
         "majorDimension": "ROWS",     
         "values": [
                    ["B2", "C2", "D2"], 
                    ['25', "=6*6", "15"]  
                   ]}
    ]
}).execute()

