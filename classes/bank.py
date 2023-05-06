
# Each class should have one class attribute and three instance variables.
"""
Then do the following in the interpreter 
Create two instances of each class. 
Call each of the methods you defined
"""


class Bank:
       
       availability_time = "8am - 9am"
       def __init__(self, name, location, status):
        self.name = name
        self.location = location
        self.status = status
        
       def giving_loan(self):
           return f" most {self.name} they are not fond in Africa"
       def saving(self):
           return f"all {self.name} are known for having short lifesapn"
       def withdrawing(self):
           return(f"you can tell whether a fruit is sweet by their {self.color}")


bank1 = Bank(name = "KCB", location = "Kenya", status ="private")
print(bank1.giving_loan())
print(bank1.saving())
print(bank1.withdrawing())

bank2 = Bank(name = "Equity Bank", location = "Global", status ="private")
print(bank2.giving_loan())
print(bank2.saving())
print(bank2.withdrawing())