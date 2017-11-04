#!/usr/bin/env python
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import scipy

def main():

    print("This program illustrates a chaotic function!")
    x=eval(input("Enter a number between 0 and 1: "))
    n=eval(input("How many times should this run?"))
    for i in range(n):
    	x = 3.9*x*(1-x)
    	print(x)

main()    


#note input requires ""