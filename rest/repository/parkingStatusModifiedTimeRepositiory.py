from pymongo import MongoClient, ASCENDING
from bson.son import SON

class ParkingStatusModifiedTimeRepository:
    def __init__(self):
        client = MongoClient('localhost:27017')
        self.db = client.melbourneCarpark


    def getLatestModifiedTime(self):
        return list(self.db.parking_bay_status_modified_time.find({}).limit(1).sort([("lastModifiedTimeId", ASCENDING)]))[0]