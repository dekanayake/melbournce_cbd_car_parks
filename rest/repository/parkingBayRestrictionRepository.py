from pymongo import MongoClient
from bson.son import SON

class ParkingBayRestrictionRepository:
    def __init__(self):
        client = MongoClient('localhost:27017')
        self.db = client.melbourneCarpark


    def getAvailableParkingBayRestrictions(self, bayIds, day, currentTime):
        return self.db.parking_restriction.find({
                "bay_id":{"$in":bayIds},
                "day":day,
                "startTime":{"$lte":currentTime},
                "endTime":{"$gte":currentTime}
            })
