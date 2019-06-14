from datetime import datetime
from domain.availableParkingBay import AvailableParkingBay
from repository.parkingBayRepository import ParkingBayRepository
from repository.parkingStatusRepository import ParkingStatusRepository
from repository.parkingBayRestrictionRepository import ParkingBayRestrictionRepository
from repository.parkingStatusModifiedTimeRepositiory import ParkingStatusModifiedTimeRepository

class ParkingBayService:
    def __init__(self):
        self.parking_bay_repository = ParkingBayRepository()
        self.parking_status_repository = ParkingStatusRepository()
        self.parking_bay_restriction_repository = ParkingBayRestrictionRepository()
        self.parking_status_modified_time_repository = ParkingStatusModifiedTimeRepository()


    def getAvailableParkingBays(self, longitude, lattitude):
        current_time = datetime.now().time()
        current_day = datetime.now().date().weekday()
        parkingStatusLastModifiedTime = self.parking_status_modified_time_repository.getLatestModifiedTime()
        parkingBayStatusList = self.__getAvailableParkingBays(longitude,lattitude, parkingStatusLastModifiedTime['lastModifiedTimeId'])
        bayIds = self.__extractBayIds(parkingBayStatusList)
        parkingRestrictions = self.__getParkingRestrictions(bayIds, current_day, current_time)
        markerIds = self.__extractStreetMarkerIds(parkingBayStatusList)
        parkingBays = self.__getParkingBays(markerIds)
        availableParkingBays = []
        for parkingBayStatus in parkingBayStatusList:
            availableParkingBay = AvailableParkingBay(
                parkingBayStatus['bay_id'],
                parkingBayStatus['location']['coordinates'][0],
                parkingBayStatus['location']['coordinates'][1],
                self.__getParkingRestrictionDescription(parkingBayStatus['bay_id'], parkingRestrictions),
                self.__getParkingBayDescription(parkingBayStatus['streetMarkerId'], parkingBays)
            )
            availableParkingBays.append(availableParkingBay)
        return availableParkingBays

    def __getParkingRestrictionDescription(self, bayId, parkingRestrictions):
        for parkingRestriction in parkingRestrictions:
            if parkingRestriction['bay_id'] == bayId:
                print(parkingRestriction)
                return parkingRestriction['description']
        return None

    def __getParkingBayDescription(self, markerId, parkingBays):
        for parkingBay in parkingBays:
            if parkingBay['marker_id'] == markerId:
                print(parkingBay)
                return parkingBay['description']
        return None

    def __getAvailableParkingBays(self, longitude, lattitude, lastModifiedTimeId):
        return self.parking_status_repository.getAvailableParkingSlots(longitude, lattitude, lastModifiedTimeId)

    def __getParkingBays(self, markerIds):
        return self.parking_bay_repository.getAvailableParkingBays(markerIds)

    def __getParkingRestrictions(self, bayIds, day, currentTime):
        date = datetime(1900, 1, 1)
        currentTime = datetime.combine(date, currentTime)
        return self.parking_bay_restriction_repository.getAvailableParkingBayRestrictions(bayIds, day, currentTime)

    def __extractBayIds(self, parkingBayStatusList):
        parkingBayIds = []
        for parkingBayStatus in parkingBayStatusList:
            parkingBayIds.append(parkingBayStatus['bay_id'])
        return parkingBayIds

    def __extractStreetMarkerIds(self, parkingBayStatusList):
        markerIds = []
        for parkingBayStatus in parkingBayStatusList:
            markerIds.append(parkingBayStatus['streetMarkerId'])
        return markerIds
