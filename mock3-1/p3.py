def f(uid):
    # Use a set to track the user IDs (case-sensitive) seen so far
    seen = set()
    
    # Iterate over each ID in the input list
    for user_id in uid:
        # If the ID is already in the set, return False (not unique)
        if user_id in seen:
            return False
        # Otherwise, add the ID to the set
        seen.add(user_id)
    
    # If no duplicates were found, return True (all IDs are unique)
    return True

# Example usage
print(f(["john5", "ann123", "JOHN5", "xxx", "abc333", "a10"]))  # Output: True
print(f(["abc123", "ann", "abc123", "a10"]))                   # Output: False
print(f(["bob2", "bob2"]))                                     # Output: False
print(f(["bob2", "BOB2"]))                                     # Output: True



# def f(uid):
#     seen = []  # Use a list to track seen identifiers
#     for user_id in uid:
#         if user_id in seen:  # Check if the ID is already in the list
#             return False
#         seen.append(user_id)  # Add the ID to the list
#     return True

# # Examples:
# print(f(["john5", "ann123", "JOHN5", "xxx", "abc333", "a10"]))  # True
# print(f(["abc123", "ann", "abc123", "a10"]))                   # False
# print(f(["bob2", "bob2"]))                                     # False
# print(f(["bob2", "BOB2"]))                                     # True
