import math

class Circle:
    def __init__(self, radius):
        """
        Initializes a Circle object with the given radius.

        Parameters:
        - radius (float): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Computes and prints the area of the circle.

        Returns:
        - float: The area of the circle.
        """
        circle_area = math.pi * self.radius**2
        print(f"The area of the circle with a radius of {self.radius} is: {circle_area:.2f}")
        return circle_area

    def perimeter(self):
        """
        Calculates and prints the perimeter (circumference) of the circle.

        Returns:
        - float: The perimeter of the circle.
        """
        circle_perimeter = 2 * math.pi * self.radius
        print(f"The perimeter of the circle with a radius of {self.radius} is: {circle_perimeter:.2f}")
        return circle_perimeter

# Get user input for the radius
radius = float(input("Please enter the radius of the circle: "))

# Create an instance of the Circle class
circle_instance = Circle(radius)

# Calculate and print the area and perimeter of the circle
circle_instance.area()
circle_instance.perimeter()
