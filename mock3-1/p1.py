

def f(word):
    # If the input word is empty, return an empty string
    if not word:
        return ""
    
    # Create a list to store each variation of the word
    wave = []
    
    # Iterate over each character in the word by index
    for i in range(len(word)):
        # Capitalize the current character and make the rest lowercase
        # Add the variation to the wave list
        wave.append(word[:i].lower() + word[i].upper() + word[i+1:].lower())
    
    # Join the variations with a '-' and return the result
    return "-".join(wave)

# Example usage
print(f("book"))  # Output: "Book-bOok-boOk-booK"
print(f("water"))  # Output: "Water-wAter-waTer-watEr-wateR"
print(f("ok"))     # Output: "Ok-oK"
print(f("a"))      # Output: "A"
print(f(""))       # Output: ""
