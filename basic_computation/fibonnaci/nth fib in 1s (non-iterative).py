import math
import time

def fibonnaci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
         return fibonnaci(n-1) + fibonnaci(n-2)



def find_max_time():
    n = 1
    while True:
        start_time = time.time()
        fibonnaci(n)
        end_time = time.time()
        run_time = end_time - start_time

        if run_time < 1:
            n +=1
        else:
            break 

    return n-1

print(find_max_time())