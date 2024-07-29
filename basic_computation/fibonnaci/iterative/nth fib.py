import math

def fib(n, memo={}):
    if n == 1 or n == 2:
        return 1
    elif n > 2:
        return fib(n-1) + fib(n-2)
    

user_number = int(input("What fibonnaci number would you like to compute?: "))
print(fib(user_number))