# month.py 

def main():
	
    #one long string 
	months="JanFebMarAprMayJunJulAugSepOctNovDec"


	n=eval(input("Enter a month number (1-12): "))



	#compure starting position of month n 

	pos= (n-1)*3


	monthAbbrev=months[pos:pos+3]


	print("The month abbreviation is ", monthAbbrev + ".")



main()	