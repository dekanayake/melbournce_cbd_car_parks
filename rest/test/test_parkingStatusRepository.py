import unittest
from rest.repository.parkingStatusRepository import ParkingStatusRepository
from rest.repository.parkingBayRepository import ParkingBayRepository
from rest.repository.parkingBayRestrictionRepository import ParkingBayRestrictionRepository
from rest.repository.parkingStatusModifiedTimeRepositiory import ParkingStatusModifiedTimeRepository
from datetime import time,datetime

class TestParkingStatusRepository(unittest.TestCase):

    def test_get_available_parking_slots(self):
        lastModifiedTimeRepository = ParkingStatusModifiedTimeRepository()
        parkingStatusRepository = ParkingStatusRepository()
        last_modified_time = lastModifiedTimeRepository.getLatestModifiedTime()
        slots = parkingStatusRepository.getAvailableParkingSlots( 144.96488490609,-37.7945695473976,last_modified_time['lastModifiedTimeId'])
        print('finding the slots')
        for doc in slots:
            print(doc)


    def test_get_parking_bays(self):
        repository = ParkingBayRepository()
        bays = repository.getAvailableParkingBays(["2118N"])
        print('finding the bays')
        for doc in bays:
            print(doc)

    def test_get_parking_restrictions(self):
        repository = ParkingBayRestrictionRepository()
        restrictions = repository.getAvailableParkingBayRestrictions(["1741"],1,datetime(1900, 1, 1, 5, 00, 00))
        print('finding the restrictions')
        for doc in restrictions:
            print(doc)


    def test_get_latest_modified_time(self):
        repository = ParkingStatusModifiedTimeRepository()
        last_modified_time = repository.getLatestModifiedTime()
        print('finding the last modified time')
        print(last_modified_time)


if __name__ == '__main__':
    unittest.main()
