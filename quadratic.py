#quadratic.py

#Solves the quadratic equation

#Crashes if no real roots 

import math

def main():
	print("This program fins the real solutions to a quadratic ")
	print()


	a, b, c = eval(input(" please eneter coefficients a,b,c : "))

	discRoot = math.sqrt(b*b-4*a*c)
	root1 = (-b + discRoot)/(2*a)
	root2 = (-b - discRoot)/(2*a)

	print()
	print("The solutions are: ", root1,root2)

main()
