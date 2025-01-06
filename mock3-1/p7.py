def f(arr2D):
    # Calculate the sum of each column and store the sums in a list
    column_sums = []
    
    # Iterate over the columns
    for col in zip(*arr2D):
        column_sums.append(sum(col))
    
    # Check if there are at least two columns with the same sum
    return len(column_sums) != len(set(column_sums))

# Example usage
print(f([[3, 4, 2], [5, 1, 6]]))  # Output: True
print(f([[3, 4, 2], [5, 1, 7]]))  # Output: False
print(f([[3, 4], [5, 1], [4, 7]]))  # Output: True
print(f([[3, 4], [5, 9], [4, 7]]))  # Output: False
