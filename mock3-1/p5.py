class C:
    def __init__(self, initial_value):
        """Initialize the counter with the given initial value."""
        self.value = initial_value

    def m1(self):
        """Return the current counter value."""
        return self.value

    def m2(self):
        """Increase the counter value by 1."""
        self.value += 1

    def m3(self):
        """Decrease the counter value by 1."""
        self.value -= 1

    def m4(self, n):
        """Increase or decrease the counter value by n."""
        self.value += n

    def __str__(self):
        """Return the string representation of the counter value."""
        return str(self.value)

# Example usage
c = C(5)
print(c.m1())  # Output: 5
c.m2()
print(c.m1())  # Output: 6
c.m4(-8)
print(c.m1())  # Output: -2
c.m3()
print(c.m1())  # Output: -3
c.m4(10)
print(c.m1())  # Output: 7
print(c.__str__())  # Output: "7"
