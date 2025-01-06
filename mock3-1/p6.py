import re

def f(vname):
    """
    Check if the variable name is valid based on the given rules.
    """
    # Define a regular expression for valid variable names
    pattern = r'^[a-zA-Z_][a-zA-Z0-9_]{0,4}$'
    
    # Match the input variable name against the pattern
    return bool(re.match(pattern, vname))

# Example usage
print(f("abc"))      # Output: True
print(f("Abc"))      # Output: True
print(f("aBC"))      # Output: True
print(f("_ab_c"))    # Output: True
print(f("abcdef"))   # Output: False
print(f("8abc"))     # Output: False
print(f("_aB8_"))    # Output: True
print(f("_4x"))      # Output: True
