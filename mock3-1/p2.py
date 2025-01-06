def f(x, y, digit):
    # Ensure the digit is a string for comparison
    digit = str(digit)
    
    # Initialize a counter to store the total occurrences of the digit
    count = 0
    
    # Iterate through each number in the range from x to y (inclusive)
    for num in range(x, y + 1):
        # Convert the current number to a string and count the occurrences of the digit
        count += str(num).count(digit)
    
    return count

# Example usage
print(f(10, 15, 1))  # Output: 7
print(f(28, 32, 2))  # Output: 3
print(f(100, 105, 6))  # Output: 0
print(f(100, 101, 0))  # Output: 3
