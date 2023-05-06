

# Each class should have one class attribute and three instance variables.
"""
Then do the following in the interpreter 
Create two instances of each class. 
Call each of the methods you defined
"""


class Fruit:
       ripeness = True
       def __init__(self, name, taste, color):
        self.name = name
        self.taste = taste
        self.color = color
        
       def availability(self):
           return f" most {self.name} they are not fond in Africa"
       def lifespan(self):
           return f"all {self.name} are known for having short lifesapn"
       def visual(self):
           return(f"you can tell whether a fruit is sweet by their {self.color}")


fruit1 = Fruit(name = "banana", taste = "sweet", color = "yellow")
print(fruit1.availability())
print(fruit1.lifespan())
print(fruit1.visual())

fruit2 = Fruit(name = "lemon", taste = "sour", color = "green")
print(fruit2.availability())
print(fruit2.lifespan())
print(fruit2.visual())



