def f(n):
    # Convert the number to a string to easily iterate over its digits
    odd_digits = [int(digit) for digit in str(n) if int(digit) % 2 != 0]
    
    # If no odd digits are found, return -1
    if not odd_digits:
        return -1
    
    # Return the difference between the largest and smallest odd digit
    return max(odd_digits) - min(odd_digits)

# Example usage
print(f(10852))      # Output: 4
print(f(723597))     # Output: 6
print(f(4388))       # Output: 0
print(f(846206))     # Output: -1
