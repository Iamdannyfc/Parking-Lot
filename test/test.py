from ..services.service import ParkingLot
import unittest

class TestParkingLot(unittest.TestCase):
    def setUp(self):
        self.parking_lot = ParkingLot("PR1234", 2, 6)
        # Park some vehicles for testing
        self.parking_lot.park_vehicle("Car", "ABC123", "Red")
        self.parking_lot.park_vehicle("Bike", "XYZ456", "Black")
        self.parking_lot.park_vehicle("Truck", "T123", "White")

    def test_create_parking_lot(self):
        # Check if the parking lot is created with the correct number of floors and slots per floor
        self.assertEqual(len(self.parking_lot.slots), 2)
        #print(self.parking_lot.slots)
        self.assertEqual(len(self.parking_lot.slots[1]), 6)
        self.assertEqual(len(self.parking_lot.slots[2]), 6)

    def test_display_free_count(self):
        # Check the count of free slots for each vehicle type
        self.parking_lot.display('free_count', 'Car')
        self.parking_lot.display('free_count', 'Bike')
        self.parking_lot.display('free_count', 'Truck')

    def test_display_free_slots(self):
        # Check the list of free slots for each vehicle type
        self.parking_lot.display('free_slots', 'Car')
        self.parking_lot.display('free_slots', 'Bike')
        self.parking_lot.display('free_slots', 'Truck')

    def test_display_occupied_slots(self):
        # Check the list of occupied slots for each vehicle type
        self.parking_lot.display('occupied_slots', 'Car')
        self.parking_lot.display('occupied_slots', 'Bike')
        self.parking_lot.display('occupied_slots', 'Truck')

if __name__ == '__main__':
    unittest.main()








