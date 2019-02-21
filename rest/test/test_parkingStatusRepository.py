import unittest
from repository.parkingStatusRepository import ParkingStatusRepository

class TestParkingStatusRepository(unittest.TestCase):

    def test_get_available_parking_slots(self):
        repository = ParkingStatusRepository()
        slots = repository.getAvailableParkingSlots(-37.808905,145.1965732)
        print('finding the slots')
        print(slots)


if __name__ == '__main__':
    unittest.main()
