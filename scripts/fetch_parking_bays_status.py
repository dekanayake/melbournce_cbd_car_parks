import requests
import json
from datetime import time,datetime
from mongoengine import *
import uuid

class ParkingBayStatus(Document):
    bay_id = StringField()
    status = StringField()
    location = PointField()
    streetMarkerId = StringField()
    lastModifiedTimeId = StringField()
    meta = {
        'indexes': [
            'bay_id',
            'streetMarkerId'
        ]
    }

class ParkingBayStatusModifiedTime(Document):
    modifiedTime = DateTimeField()
    lastModifiedTimeId = StringField()

url = 'https://data.melbourne.vic.gov.au/resource/vh2v-4nfs.json?$limit=50000'
headers = {'X-App-Token': '2rKRf7vDTZdViV0k15XJuBBTH'}

resp = requests.get(url, headers=headers)
last_modified_time = datetime.strptime(resp.headers['Last-Modified'], '%a, %d %b %Y %H:%M:%S GMT')
modifiedTimeId = uuid.uuid4()

connect('melbourneCarpark', host='localhost', port=27017)
for feature in resp.json():
    parkingBayStatus = ParkingBayStatus()
    parkingBayStatus.bay_id = feature['bay_id']
    parkingBayStatus.location = [float(feature['location']['longitude']),float(feature['location']['latitude'])]
    parkingBayStatus.status = feature['status']
    parkingBayStatus.streetMarkerId = feature['st_marker_id']
    parkingBayStatus.lastModifiedTimeId = modifiedTimeId.hex
    parkingBayStatus.save()

parkingBayStatusModifiedTime = ParkingBayStatusModifiedTime()
parkingBayStatusModifiedTime.modifiedTime = last_modified_time
parkingBayStatusModifiedTime.lastModifiedTimeId = modifiedTimeId.hex
parkingBayStatusModifiedTime.save()
