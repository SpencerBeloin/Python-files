# Sphere.py


import math


def main():

	print("This program calculates volume and surface area of a sphere: ")


	print()


	r=eval(input("Please enter a radius : "))


	volume= (4.0//3.0)*math.pi*r**3


	surface = 4*math.pi*r**2


	print()

	print("volume of the sphere is ",volume)
	print("surface area of sphere is ", surface)



main()	