
from ..services.service import ParkingLot
# Here, what do you want from the parking lot 



# Run to interact on command line
if __name__ == "__main__":
    while True:
        # Input command
        command = input("What would you like to do? ")
        parts = command.split()
        if parts[0] == "create_parking_lot":
            parking_lot_id, no_of_floors, no_of_slots_per_floor = parts[1], int(parts[2]), int(parts[3])
            # Create a new ParkingLot object
            parking_lot = ParkingLot(parking_lot_id, no_of_floors, no_of_slots_per_floor)
            print(f"Created parking lot with {no_of_floors} floors and {no_of_slots_per_floor} slots per floor")
        elif parts[0] == "park_vehicle":
            if parking_lot:
                # Park the vehicle and print the result
                print(parking_lot.park_vehicle(parts[1], parts[2], parts[3]))
        elif parts[0] == "unpark_vehicle":
            if parking_lot:
                # Unpark the vehicle using ticket ID and print the result
                print(parking_lot.unpark_vehicle(parts[1]))
        elif parts[0] == "display":
            if parking_lot:
                # Display information about free or occupied slots based on the display type and vehicle type
                parking_lot.display(parts[1], parts[2])
        elif parts[0] == "exit":
            break
