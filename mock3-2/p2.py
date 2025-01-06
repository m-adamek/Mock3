def f(x, y, d):
    # Iterate through each number in the range from x to y (inclusive)
    for num in range(x, y + 1):
        # Convert the number to a string and check if the substring d appears in it
        if d in str(num):
            return True
    # If no match is found, return False
    return False

# Example usage
print(f(10, 15, "14"))  # Output: True
print(f(100, 120, "11"))  # Output: True
print(f(205, 210, "04"))  # Output: False
