class Vehicle:
    def __init__(self, vehicle_type, reg_no, color):
        """
        Initializes a Vehicle object with type, registration number, and color.
        
        Args:
        - vehicle_type (str): Type of the vehicle (Car, Bike, Truck).
        - reg_no (str): Registration number of the vehicle.
        - color (str): Color of the vehicle.
        """
        self.vehicle_type = vehicle_type
        self.reg_no = reg_no
        self.color = color

class ParkingLot:
    def __init__(self, parking_lot_id, no_of_floors, no_of_slots_per_floor):
        """
        Initializes a ParkingLot object with ID, number of floors, and number of slots per floor.
        
        Args:
        - parking_lot_id (str): Unique identifier for the parking lot.
        - no_of_floors (int): Number of floors in the parking lot.
        - no_of_slots_per_floor (int): Number of slots per floor in the parking lot.
        """
        self.parking_lot_id = parking_lot_id
        self.no_of_floors = no_of_floors
        self.no_of_slots_per_floor = no_of_slots_per_floor
        # Initialize slots dictionary with None values for each slot in each floor
        self.slots = {floor: {slot: None for slot in range(1, no_of_slots_per_floor + 1)} for floor in range(1, no_of_floors + 1)}

    def park_vehicle(self, vehicle_type, reg_no, color):
        """
        Parks a vehicle in the parking lot if a suitable slot is available.
        
        Args:
        - vehicle_type (str): Type of the vehicle to be parked.
        - reg_no (str): Registration number of the vehicle.
        - color (str): Color of the vehicle.

        """
        # Iterate over each floor and slot to find the first available slot
        for floor in range(1, self.no_of_floors + 1):
            for slot in range(1, self.no_of_slots_per_floor + 1):
                # Skip slots based on vehicle type and slot position rules
                if slot == 1 and vehicle_type != "Truck":
                    continue
                elif slot in [2, 3] and vehicle_type != "Bike":
                    continue
                # Park the vehicle if the slot is available
                if self.slots[floor][slot] is None:
                    self.slots[floor][slot] = Vehicle(vehicle_type, reg_no, color)
                    return f"Parked vehicle. Ticket ID: {self.parking_lot_id}_{floor}_{slot}"
        return "Parking Lot Full"

    def unpark_vehicle(self, ticket_id):
        """
        Unparks a vehicle from the parking lot using the ticket ID.
        
        Args:
        - ticket_id (str): Ticket ID of the vehicle to be unparked.
        
        Returns:
        - str: Message indicating success or failure of unparking operation.
        """
        parts = ticket_id.split('_')
        floor, slot = int(parts[1]), int(parts[2])
        # Check if the slot is occupied and unpark the vehicle
        if self.slots[floor][slot]:
            reg_no = self.slots[floor][slot].reg_no
            color = self.slots[floor][slot].color
            self.slots[floor][slot] = None
            return f"Unparked vehicle with Registration Number: {reg_no} and Color: {color}"
        else:
            return "Invalid Ticket"

    def display(self, display_type, vehicle_type):
        """
        Displays information about free and occupied slots in the parking lot.
        
        Args:
        - display_type (str): Type of display (free_count, free_slots, occupied_slots).
        - vehicle_type (str): Type of vehicle to filter the display.
        """
        if display_type == 'free_count':
            # Iterate over each floor to count free slots for the specified vehicle type
            for floor in range(1, self.no_of_floors + 1):
                count = 0
                for slot in range(1, self.no_of_slots_per_floor + 1):
                    # Skip slots based on vehicle type and slot position rules
                    if (slot == 1 and vehicle_type != "Truck") or (vehicle_type == "Truck" and slot > 1):
                        continue
                    elif (slot in [2, 3] and vehicle_type != "Bike") or (vehicle_type == "Bike" and slot > 3):
                        continue
                    if self.slots[floor][slot] is None:
                        count += 1
                print(f"No. of free slots for {vehicle_type} on Floor {floor}: {count}")
        elif display_type == 'free_slots':
            # Iterate over each floor to list free slots for the specified vehicle type
            for floor in range(1, self.no_of_floors + 1):
                slots = []
                for slot in range(1, self.no_of_slots_per_floor + 1):
                    # Skip slots based on vehicle type and slot position rules
                    if (slot == 1 and vehicle_type != "Truck") or (vehicle_type == "Truck" and slot > 1):
                        continue
                    elif (slot in [2, 3] and vehicle_type != "Bike") or (vehicle_type == "Bike" and slot > 3):
                        continue
                    if self.slots[floor][slot] is None:
                        slots.append(str(slot))
                print(f"Free slots for {vehicle_type} on Floor {floor}: {', '.join(slots)}")
        elif display_type == 'occupied_slots':
            # Iterate over each floor to list occupied slots for the specified vehicle type
            for floor in range(1, self.no_of_floors + 1):
                slots = [str(slot) for slot in range(1, self.no_of_slots_per_floor + 1) if self.slots[floor][slot] is not None and self.slots[floor][slot].vehicle_type == vehicle_type]
                print(f"Occupied slots for {vehicle_type} on Floor {floor}: {' '.join(slots)}")
                
                
                
                
                
                
                
                
                
                
                
                
