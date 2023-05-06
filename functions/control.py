

# Next topic \\\\\\\     Control Flow         \\\\\\ #

# Techniques for controling the order of excecution of a program

# range functions
# >>> a = range(10,100,10)
# >>> for i in a:print(i)
# if statement 

# check if a given condition/expresion/operation is true or false

def even_number():
    x = range(10)
    for i in x:
        if i % 2 == 0:
            print(i)

even_number()



def odd_number():
    x = range(20)
    for i in x:
        if i % 2 != 0:
            print(i)


# else statement

# the if statement can be combined with an operational else statement. the code inside the else statement scope
# is executed if the if statement returns false

def divisible_by_five():
    x = range(100)
    
    for i in x:
        if i % 5 == 0:
            print(f"{i} is visible by 5")
        else:
            print(f"{i} not divisible by 5")


# elif statement

# Allows us to do multiple comparisons when combined with if statement

def multiple_comparison():
    x = range(30)
    
    for i in x:
        if i % 2 == 0:
            print(f"{i} is visible by 2")
        elif i % 3 == 0:
            print(f"{i} not divisible by 3")
            
        elif i % 5 == 0:
            print(f"{i} not divisible by 5")

        else:
              print(f"{i} not divisible by 3,2,5")


# combining logic operators with elif statement 
# AND, OR ,NOT

# logical operators 

def divisible_by_two_an_three():
    x = range(30)
    
    for i in x:
        if i % 2 == 0 and i % 3 == 0:
            print(f"{i} is visible by 2 and 3")
        elif i % 2 == 0 or i % 3 == 0:
            print(f"{i} not divisible by either 2 and 3")

        else:
              print(f"{i} not divisible by 3 or 2")


# >>> True and True
# True
# >>> True and False
# False
# >>> True or True
# True
# >>> True or False
# True
# >>> False and False
# False
# >>> False and True
# False
# >>> False or False
# False
# >>> False or True
# True
# >>> 


# While Loop 
# Continues to iterate as long as a given condition is true
def while_loop():
    x = 1
    while x < 10:
        print("hello while")
        x += 1


# break starement
#  it steps the while loop from iterating even if the given condition is true

def break_statement():
    x = 1
    while x < 10:
        print("hello while")
        x += 1
        if x == 5:
            break


# continue statement
# skips the reminder of the current iteration and moves to the next iteratio

def continue_statement():
    x = 0
    while x < 20:
        x += 1
        if x %2 == 0:
            continue
        print(x)







