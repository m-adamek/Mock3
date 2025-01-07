def f(fnc, prods):
    # Use the map function to apply fnc to each product in prods
    product_ids = list(map(fnc, prods))
    # Join the resulting IDs with commas and return the string
    return ",".join(product_ids)


# Example usage
prods = ["water", "cheese", "tomato"]

fnc1 = lambda x: "id:" + x[:2]
print(f(fnc1, prods))  # Output: "id:wa,id:ch,id:to"

fnc2 = lambda x: (x[0] + x[-1]).upper()
print(f(fnc2, prods))  # Output: "WR,CE,TO"
