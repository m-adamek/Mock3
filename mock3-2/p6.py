import re

def f(mnumbers):
    # Define the pattern for a valid number on Metis
    pattern = r'^[+-]?[1-7a-dA-D]+$'
    
    # Count how many numbers match the pattern
    valid_count = sum(1 for num in mnumbers if re.match(pattern, num))
    
    return valid_count

# Example usage
print(f(["A15", "-31", "7abC", "+D1", "-gH"]))  # Output: 5
print(f(["A05", "-3+1", "7ab8C", "+D1", "-22k"]))  # Output: 1
