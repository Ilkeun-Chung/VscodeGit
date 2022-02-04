#!/usr/bin/env python3

import sys
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = [
'https://spreadsheets.google.com/feeds',
'https://www.googleapis.com/auth/drive',
]
json_file_name = './resounding-axe-306509-71a6f3c0cf51.json'

# macbook
#gc = gspread.authorize(credentials)

# linux
gc = gspread.service_account(filename='./resounding-axe-306509-71a6f3c0cf51.json')

spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1Apip23ydyUiybGksEzXBU-cxmH5fPcMFRiD6iQWv-Cw/edit#gid=1846671570'
doc = gc.open_by_url(spreadsheet_url)


return_val = sys.argv[1]
worksheet = doc.worksheet('36F IP')
worksheet.update_acell('A4', return_val)

