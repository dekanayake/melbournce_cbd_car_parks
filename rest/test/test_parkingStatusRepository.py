import unittest
from repository.parkingStatusRepository import ParkingStatusRepository
from repository.parkingBayRepository import ParkingBayRepository
from repository.parkingBayRestrictionRepository import ParkingBayRestrictionRepository
from datetime import time,datetime

class TestParkingStatusRepository(unittest.TestCase):

    def test_get_available_parking_slots(self):
        repository = ParkingStatusRepository()
        slots = repository.getAvailableParkingSlots( 144.96488490609,-37.7945695473976)
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


if __name__ == '__main__':
    unittest.main()
