def f(d):
    # Create a set to keep track of vehicles in the car park
    parked_vehicles = set()

    # Loop through each entry in the list
    for car, action in d:
        if action == "in":
            # Add the car to the car park
            parked_vehicles.add(car)
        elif action == "out":
            # Remove the car from the car park
            parked_vehicles.discard(car)

    # Return the sorted list of vehicles that remain in the car park
    return sorted(parked_vehicles)

# Example usage
cars = [["KR234", "in"], ["BA123", "in"], ["GX444", "in"], ["KR234", "out"], 
        ["BA111", "in"], ["BA123", "out"], ["KR234", "in"]]
print(f(cars))  # Output: ["BA111", "GX444", "KR234"]

cars1 = [["KR234", "in"], ["KR234", "out"]]
print(f(cars1))  # Output: []
