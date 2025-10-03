class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        """
        Initialize the parking system with the number of available spots 
        for each car type.

        Args:
            big (int): number of available big car parking spots
            medium (int): number of available medium car parking spots
            small (int): number of available small car parking spots
        """
        # Store available spaces in a list:
        # index 0 -> big, index 1 -> medium, index 2 -> small
        self.spaces = [big, medium, small]
        

    def addCar(self, carType: int) -> bool:
        """
        Attempts to park a car of the given type.

        Args:
            carType (int): type of car to add
                1 -> big
                2 -> medium
                3 -> small

        Returns:
            bool: True if a parking spot is available and car is parked,
                  False if no spot is available.
        """
        # Check if there is at least one available space 
        # for the given car type (carType - 1 is used since list is 0-indexed).
        if self.spaces[carType - 1] > 0:
            # Decrement the available space count for that car type
            self.spaces[carType - 1] -= 1
            return True  # successfully parked
        
        # No spots available for this car type
        return False


# Example usage:
# obj = ParkingSystem(1, 1, 0)  # 1 big spot, 1 medium, 0 small
# print(obj.addCar(1))  # True (parks in big)
# print(obj.addCar(2))  # True (parks in medium)
# print(obj.addCar(3))  # False (no small spots available)