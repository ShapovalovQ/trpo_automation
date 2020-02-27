# coding: utf-8

def AddMarkInTable(table, cell):
    import httplib2 
    import apiclient.discovery
    from oauth2client.service_account import ServiceAccountCredentials	

    try:
        #Ключ API для работы
        CREDENTIALS_FILE = 'myJson.json' 

        credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'])

        httpAuth = credentials.authorize(httplib2.Http())
        service = apiclient.discovery.build('sheets', 'v4', http = httpAuth) 

        #Id таблицы
        spreadsheetId = '1Hq6BrKSUtFnIV0_rdCaiH36s2NwdIbobTImhJnbeGOE'
          
        rangeTab = str(table) + "!" + str(cell)

        #Сам метод добавления
        #Если пиздец! То лазить тут!
        service.spreadsheets().values().batchUpdate(spreadsheetId = spreadsheetId, body = {
            "valueInputOption": "USER_ENTERED",
            "data": [
                {"range": rangeTab,
                 "majorDimension": "ROWS",     
                 "values": [ ["1"] ]
                }
            ]
        }).execute()
    except e: 
        print("Error Function AddMarkInTable!" + e)

