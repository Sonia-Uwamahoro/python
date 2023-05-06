

# To create a function that can accept any number of positional arguments, we define the function with only one
# parameter but with a star on it before the parameter name.
# they are converted into a list

def hello(*names):
    for name in names:
        rgb = ','.join(name)
        print(rgb)


def sum(*numbers):
    answer = 0
    for number in numbers:
        answer += number
    return answer


# write a function that accpets any numbers of integers and returns the results of multiply of all of them

def multiply(*numbers):
    answer = 1
    for number in numbers:
        answer *= number
    return answer

multiply(2,3,4,1,3)



# write a function that accpets any numbers of keyword arguments
# we define the function with one parameter but with 2 stars
# they are converted into a dictionary
# a function that can accept any number of attributed like it intake more than one data

def student_attributes(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")

# -- Default arguments -- #
# we can define a function with a parameter that has a default value. if no argument is passed when the function
# invoked it will default value in place. 

def my_country(country = "Burundi"):
    print(f"hello from {country}")



# Functional Arguments


# A function named concatenate_args that takes any number of string arguments in positional arguments 
# format and concatenates them into a single string
def colors(*names):
        rainbow_colors = ','.join(names)
        print(rainbow_colors)





# A function named concatenate_kwargs that takes any number of string arguments in keyword arguments  
# format and concatenates them into a single string
def concatenate_kwargs(**kwargs):
    languages = ""
    for key, value in kwargs.items():
        languages += (f"{key}:{value}")
    print(languages)














