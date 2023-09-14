import requests
import pandas as pd


url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
api_key = "AIzaSyBrgYTurxFHyCg6xvzLB1KJD5S3r1EGzic"


cities = ["Berlin", "Hamburg", "Munich", "Cologne", "Frankfurt", "Stuttgart", "Düsseldorf", "Dortmund", "Essen", "Leipzig"]
queries = [
    ("Solar Energy", "Solar"),
    ("Wind Energy", "Wind"),
    ("Hydropower", "Hydropower"),
    ("Biomass Energy", "Biomass"),
    ("Geothermal Energy", "Geothermal"),
    ("Bioenergy", "Bioenergy"),
    ("Ocean Energy", "Ocean"),
    ("Hydrogen Energy", "Hydrogen"),
    ("Waste-to-Energy", "Waste-to-Energy"),
    ("Tidal Energy", "Tidal")
]


company_details = []


for city in cities:
    for query, energy_type in queries:
        params = {
            "query": query + " in " + city,
            "key": api_key
        }

        response = requests.get(url, params=params)
        data = response.json()

        if "results" in data:
            results = data["results"]
            for result in results:
                name = result["name"]
                address = result["formatted_address"]
                place_id = result["place_id"]

                company_info = {"City": city, "Name": name, "Formatted Address": address, "Place ID": place_id, "Type": energy_type}

                company_details.append(company_info)

df = pd.DataFrame(company_details)

df.to_excel("companies_data1.xlsx", index=False)