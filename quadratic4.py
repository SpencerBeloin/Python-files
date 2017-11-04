#quadratic4.py 

import math 

def main():

    print("This program finds the real solutions of a quadratic")


    print()

    a,b,c = eval(input(" Please enter the coefficients ( a, b, c) : "))

    discrim = b*b - 4*a*c

    if discrim < 0:
       print(" The equation has no real roots!" )

    elif discrim == 0:
      
       root = -b/(2*a)
       print(" There is a double root at", root)

    else:
       discRoot = math.sqrt( b*b -4*a*c)
       root1 = (-b + discRoot)/ (2*a)

       root2 = (-b - discRoot)/ (2*a)
       
       print("The solutions are: ", root1,root2)


main()