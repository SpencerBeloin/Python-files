#factorial.py 

#computes a factorial using reassignment of a variable

def main():
  
    n= eval(input("Please enter a whole number: "))
    fact = 1
 
	for factor in range(n,1,-1):
		fact = fact*factor
    print fact

main()
