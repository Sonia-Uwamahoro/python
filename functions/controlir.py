
# Write a function that uses while, if and continue statements 
# to print all the even numbers between 0 and 50. 

# def even_number():
#     x = 0
#     while x < 50:
#         x += 1
#         if x%2 != 0:
#             continue
#         print(x)
# even_number()





# Write a function that takes an integer argument and prints "Prime" if 
# the number is prime, and "Not prime" if the number is not prime.

def checking_number():
    num = 21
    if num > 1:
        for i in range(2,int(num/2)+1):
            if(num % i) == 0:
                print(num, "is not prime number")
                break
        else:
            print(num, "is a prime number")
checking_number()

# Write a function that takes a list of integers as input and prints the sum of all the even numbers in the list.

def list_of_integers():
    list =  [1,2,3,4,5,6,7,8,9]
    sum = 0
    for i in list:
        if i % 2 == 0:
            sum += i
        print(sum)
    

# Write a function that takes any two integers as input, and prints the sum of all the numbers between the two integers (inclusive) that are divisible by 3.

not_n = []
with_n = []
def inputts(n, m):
    for x in range(1, m+1):
        if x % 3 == 0:
            with_n.append(x)
        else:
           not_n.append(x)
    nott_n = sum(not_n)
    withh_n = sum(with_n)
    
    subb=(withh_n-nott_n)
    print(abs(subb))

inputts(5,20)