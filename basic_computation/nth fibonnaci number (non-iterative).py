import math
import time

def fibonnaci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
         return fibonnaci(n-1) + fibonnaci(n-2)

nth_fibonnaci_number = int(input("What is the nth fibonacci number?: "))
print(fibonnaci(nth_fibonnaci_number))