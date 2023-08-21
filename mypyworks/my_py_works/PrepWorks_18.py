'''
Write a parent class Vehicle with attributes brand,year,color and inherit subclasses motorcycle,car and truck. 
The subclasses must have a method honk() that plays the following sounds in the computer
'''
from playsound import playsound
class Vehicle():
    def __init__(self,brand,year,color):
        self.brand = brand
        self.year = year
        self.color = color
    
class Motorcycle(Vehicle):
    def __init__(self,brand,year,color,body):
        super().__init__(brand,year,color)
        self.body = body
        print(self.body)
    def honk(self):
        filename = "C:\git\MyProjects\mypyworks\my_py_works\motorbike.mp3"
        print(f"Playing {filename}..............................")
        playsound(filename)

class Car(Vehicle):
    def __init__(self,brand,year,color):
        super().__init__(brand,year,color)
        print(self.brand)
    def honk(self):
        filename = "C:\git\MyProjects\mypyworks\my_py_works\car.mp3"
        print(f"Playing {filename}..............................")
        playsound(filename)

class Truck(Vehicle):
    def __init__(self,brand,year,color):
        super().__init__(brand,year,color)
        print(self.color)
    def honk(self):
        filename = rf"C:\git\MyProjects\mypyworks\my_py_works\truck.mp3"
        print(f"Playing {filename}..............................")
        playsound(filename)

#veh = Vehicle('TATA','2023','blue')
motor = Motorcycle('Yamaha','2018','red','steel')
print(motor)
#car = Car('Nissan','2016','white')
#truck = Truck('RAM','2023','Blue')
#motor.honk()
#car.honk()
#truck.honk()