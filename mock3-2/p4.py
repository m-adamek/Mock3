def f(fnc, res):
    # Filter the results based on the given function fnc
    filtered_res = list(filter(fnc, res))
    
    # If the filtered list is empty, return 0 (or any value you prefer for no valid results)
    if not filtered_res:
        return 0
    
    # Calculate and return the difference between the highest and lowest test results
    return max(filtered_res) - min(filtered_res)

# Example usage
res = [95, 90, 20, 50, 70]

fnc1 = lambda x: x > 50
print(f(fnc1, res))  # Output: 25

fnc2 = lambda x: x > 30 and x < 90
print(f(fnc2, res))  # Output: 20
