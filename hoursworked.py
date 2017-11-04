#hoursworked.py



import math


n=eval(input("Please enter number of hours worked: "))




if(n<40):

	print( "you earned ", n*10 , "dollars this week")


else:
	
	print( "you earned" , 400+(n-40)*15 , "dollars this week")	