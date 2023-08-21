#Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter
import math
class Circle():
    def __init__(self,radius):
        self.radius =radius

    def area(self):
        area = math.pi * self.radius**2
        print(area)

    def peri(self):
        perimeter = 2* math.pi * self.radius
        print(perimeter)

mycir = Circle(radius =5)
mycir.area()
mycir.peri()