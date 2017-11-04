
#  function for testin trig in python 

import math



def main():
	print("Testing trig functions ")
	print()


		# if a and be are equal value should = math.sqrt(c)?
		# SUCCESS it does! 
    	a, b, c = eval(input(" please eneter coefficients a,b,c : "))


    	value=math.sqrt(c*math.cos(a)**2+c*math.sin(b)**2)


	print()
	print("sqrt(c) : ", value, math.sqrt(c))

main()
