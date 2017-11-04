# fibonacci.py
#-----------------------------------------------------------------------

import math

# Accept integer n as a command-line argument. Write to standard
# output the first n Fibonacci numbers.

n =eval(input("Please enter a number: "))

f = 0
g = 1

# F_n= F_n-1 + F_n-2

for i in range(0, n):
    f = f + g
    g = f - g
   

    print(f)
