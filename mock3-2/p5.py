import math

class C:
    def __init__(self, x, y):
        # Initialize the point coordinates
        self.x = x
        self.y = y

    def m1(self):
        # Determine the quadrant of the point (x, y)
        if self.x == 0 or self.y == 0:
            return 0  # Point is on the X-axis or Y-axis
        elif self.x > 0 and self.y > 0:
            return 1  # Quadrant 1
        elif self.x < 0 and self.y > 0:
            return 2  # Quadrant 2
        elif self.x < 0 and self.y < 0:
            return 3  # Quadrant 3
        elif self.x > 0 and self.y < 0:
            return 4  # Quadrant 4

    def m2(self, a, b):
        # Check if the point (x, y) and (a, b) are in the same quadrant
        return self.m1() == C(a, b).m1()

    def m3(self, a, b):
        # Calculate the distance between points (x, y) and (a, b)
        distance = math.sqrt((self.x - a)**2 + (self.y - b)**2)
        return distance > 5

# Example usage
p = C(2, 3)
print(p.m1())  # Output: 1
print(p.m2(7, 4))  # Output: True
print(p.m2(-3, 1))  # Output: False
print(p.m3(8, 5))  # Output: True
print(p.m3(4, 7))  # Output: False

p1 = C(0, 5)
print(p1.m1())  # Output: 0
print(p1.m2(4, 7))  # Output: False
print(p1.m2(-7, 0))  # Output: True
