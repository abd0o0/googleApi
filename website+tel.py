import requests
import pandas as pd

api_key = 'AIzaSyBrgYTurxFHyCg6xvzLB1KJD5S3r1EGzic'

def get_place_details(api_key, place_id):
    endpoint = 'https://maps.googleapis.com/maps/api/place/details/json'

    params = {
        'key': api_key,
        'place_id': place_id,
        'fields': 'website,international_phone_number'
    }

    try:
        response = requests.get(endpoint, params=params)
        data = response.json()

        if response.status_code == 200 and data['status'] == 'OK':
            result = data['result']
            website = result.get('website', '')
            international_phone_number = result.get('international_phone_number', '')
            return website, international_phone_number
        else:
            print('Error:', data['status'])
            return None, None

    except requests.exceptions.RequestException as e:
        print('Request error:', str(e))
        return None, None




data_frame = pd.read_excel('companies_data1.xlsx')

data_frame['Website'] = ''
data_frame['International Phone Number'] = ''

for index, row in data_frame.iterrows():
    place_id = row['Place ID']

    website, international_phone_number = get_place_details(api_key, place_id)

    data_frame.at[index, 'Website'] = website
    data_frame.at[index, 'International Phone Number'] = international_phone_number

data_frame.to_excel('companies_data1.xlsx', index=False)
