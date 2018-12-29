import requests
import json

url = 'https://data.melbourne.vic.gov.au/resource/wuf8-susg.json?$limit=50000'
headers = {'X-App-Token': '2rKRf7vDTZdViV0k15XJuBBTH'}

resp = requests.get(url, headers=headers)
with open("data_file.json", "w") as write_file:
    for feature in resp.json():
        json.dump(feature, write_file)
