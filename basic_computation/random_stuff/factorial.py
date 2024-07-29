import time 
import math 

def factorial(n, memo={}):
    memo[0] = 1
    memo[1] = 1

    if memo is None: 
        memo = {}
    if n not in memo:
        memo[n] = n * factorial(n-1, memo)
    return memo[n]

user_number = int(input("what number: "))

time_now = time.perf_counter()
print(factorial(user_number))
time_after = time.perf_counter()
run_time = time_after - time_now
print(f"It took {run_time: .15f} seconds using memoisation")

def factorial_slow(n):
     if n == 0 or n == 1:
        return 1
     if n > 1:
        return n * factorial(n-1)

time_now = time.perf_counter()

print(factorial_slow(user_number))

time_after = time.perf_counter()
rune_time = time_after - time_now
print(f"But using the built in math function it took {run_time: .15f} ")