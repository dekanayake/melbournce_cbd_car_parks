import unittest
from rest.service.parkingBayService import ParkingBayService
from pprint import pprint

class TestParkingBayService(unittest.TestCase):

    def test_get_available_parking_bays(self):
        parkingBayService = ParkingBayService()
        slots = parkingBayService.getAvailableParkingBays(144.96488490609,-37.7945695473976)
        print('>>>>>>>>>>>>>>>>>>>>>>')
        for doc in slots:
            pprint(vars(doc))
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>')


if __name__ == '__main__':
    unittest.main()
