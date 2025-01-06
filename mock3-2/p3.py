def f(d):
    # Calculate the average number of passengers across all flights
    avg_passengers = sum(d.values()) / len(d)
    
    # Count how many flights have more passengers than the average
    count = sum(1 for passengers in d.values() if passengers > avg_passengers)
    
    return count

# Example usage
print(f({"LO231": 150, "BA787": 120, "NZ15": 30}))  # Output: 2
print(f({"LO231": 150, "BA787": 20, "NZ15": 30}))   # Output: 1
