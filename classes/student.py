
# OOP (object oriented programming)
# programing paradigm that organises software in objects as opposed to just function an logic.
# Objects have attributes and behaviours.
# a class defines an object but it does not create an object. to crate an object you must create an instance of
# tha class

# class Student:
#     name = "Sonia"
#     age = 10
#     school = "AkiraChix"
#     identity = "AkiraChix"


# instances of object

# student1 = Student()
# student1.name


# student2 = Student()
# student2.name




# Instant variable

# creating a class using instance variales

class Student:
   school = "AkiraChix"

   def __init__(self, name, age, nationality):  #constructo
       self.name = name
       self.age = age
       self.nationality = nationality

   def greet_student(self):
       return f"hello {self.name}"
   
   def year_of_birth(self):
       year = 2023 - self.age
       return f"hello {self.name} you were born in {year}"

# Elizabeth = Student(name= "Elizabeth", age="22", nationality="Kenya")
# Lado = Student(name="Lado")
# Elizabeth.name


# class methods

#  methods are behaviours to classes and they oparate on the class attributes.   
# we use normal python functions         #instance
#  Elizabeth.greet_student()

class Person:
    school = "AkiraChix"
    def __init__(self, name, age, race):
        self.name = name
        self.age = age
        self.race = race

    def eating(self):
        return f"Hello {self.name}"
person1 = Student(name="sonia", age= 12, race="black")
person1.name

# 



# CLASSES ASSIGNMENT

"""
1) Update the Student Class to include these attributes - first_name, last_name, age, country
     - Add these methods to the Student class
             - show_full_name
             - year_of_birth
             - show_initials

"""

class Student:
      
      def __init__(self, first_name, last_name, age, country):
       self.first_name = first_name
       self.last_name = last_name
       self.age = age
       self.country = country


      def show_full_name(self):
       return f"{self.first_name} {self.first_name}"
   
      def year_of_birth(self):
       
       year = 2023 - self.age
       return f"Born in {year}"
      
      def show_initials(self):
         both_names = self.first_name + self.last_name
         checking_name = both_names.split()
         new = ""
         for i in range(len(checking_name) -1):
            x = checking_name[i]
            new += (x[0].upper() + '.')
            new += checking_name[-1].title()
            return new



student1 = Student(first_name = "Sonia", last_name = "Uwamahoro", age = 20, country = "Rwanda")
Student.show_full_name()
Student.year_of_birth()
Student.show_initials()
   















