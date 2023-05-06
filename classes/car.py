

# Each class should have one class attribute and three instance variables.
"""
Then do the following in the interpreter 
Create two instances of each class. 
Call each of the methods you defined
"""


class Car:
       wheel = "four"
       def __init__(self, brand, capacity, color):
        self.brand = brand
        self.capacity = capacity
        self.color = color
        
       def vehicle_horn(self):
           return f"Car {self.brand} make this horn sound tuuuuuuuuuuuuuu"
       def speed(self):
           return f"people love cars with few {self.capacity}"
       def engine(self):
           return(f"colors like {self.color}")


car1 = Car(brand="Toyota", capacity=4, color="black")
print(car1.vehicle_horn())
print(car1.speed())
print(car1.engine())

car2 = Car(name="V8", capacity=5, color="grey")
print(car2.vehicle_horn())
print(car2.speed())
print(car2.engine())









