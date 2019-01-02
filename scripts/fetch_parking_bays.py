import requests
import json
from mongoengine import *

class ParkingBay(Document):
    bay_id = StringField()
    description = StringField()
    seg_id = StringField()
    marker_id = StringField()
    the_geom = MultiPolygonField()
    meta = {
        'indexes': [
            'bay_id',
            'seg_id'
        ]
    }

url = 'https://data.melbourne.vic.gov.au/resource/wuf8-susg.json?$limit=50000'
headers = {'X-App-Token': '2rKRf7vDTZdViV0k15XJuBBTH'}

resp = requests.get(url, headers=headers)
connect('melbourneCarpark', host='localhost', port=27017)
for feature in resp.json():
    parkingBay = ParkingBay()
    parkingBay.bay_id = feature['bay_id']
    if 'rd_seg_dsc' in feature:
        parkingBay.description = feature['rd_seg_dsc']
    if 'rd_seg_id' in feature:
        parkingBay.seg_id = feature['rd_seg_id']
    if 'marker_id' in feature:
        parkingBay.marker_id = feature['marker_id']
    parkingBay.the_geom = feature['the_geom']
    parkingBay.save()
