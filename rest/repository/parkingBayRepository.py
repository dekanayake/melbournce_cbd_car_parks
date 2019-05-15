from pymongo import MongoClient
from bson.son import SON

class ParkingBayRepository:
    def __init__(self):
        client = MongoClient('localhost:27017')
        self.db = client.melbourneCarpark


    def getAvailableParkingBays(self, markerIds):
        return list(self.db.parking_bay.find({"marker_id":{"$in":markerIds}}))
