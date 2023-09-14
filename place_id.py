import os
import requests
import win32com.client as win32
import urllib.parse

API_KEY = "AIzaSyBrgYTurxFHyCg6xvzLB1KJD5S3r1EGzic"  # Replace "YOUR_API_KEY" with your actual API key

def get_place_id(name, street, postal_code):
    query = f"{name} {street} {postal_code} "
    encoded_query = urllib.parse.quote(query)
    url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={query}&key={API_KEY}"
    response = requests.get(url)
    results = response.json().get('results')
    
    if results:
        print(results)[0]
        return results[0].get('place_id')
    else:
        return None

xlApp = win32.Dispatch('Excel.Application')
xlApp.Visible = True
wb = xlApp.Workbooks.Open(os.path.join(os.getcwd(), 'Leadquelle.xlsx'))
wsList = wb.Worksheets('Sheet1')

LastRow = wsList.Cells(wsList.Rows.Count, 'A').End(-4162).Row

for i in range(2, 4):
    name = wsList.Cells(i, 1).Value
    street = wsList.Cells(i, 2).Value
    postal_code = wsList.Cells(i, 3).Value
    place_id = get_place_id(name, street, postal_code)
    wsList.Cells(i, 4).Value = place_id