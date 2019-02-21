from pymongo import MongoClient
from bson.son import SON

class ParkingStatusRepository:
    def __init__(self):
        client = MongoClient('localhost:27017')
        self.db = client.ContactDB


    def getAvailableParkingSlots(self, longitude, lattitude):
        query = {"location": SON([("$near", [longitude, lattitude]), ("$maxDistance", 1/111.12)])}
        return self.db.parking_bay_status.find({"location": {"$near": [longitude, longitude]}}).limit(100)
