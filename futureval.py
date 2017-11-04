# future_value.py
from graphics import *

def main():
	print ("This program calculates future value of an investment ")


	principal=eval(input("Enter initial principle: "))
	apr=eval(input("Enter the annual interest rate: "))
 
        win=GraphWin("Investment Growth Chart", 320, 240)
 
        win.setBackground("white")

	Text(Point(20,230),'0.0K').draw(win)
	Text(Point(20,180),'2.5K').draw(win)
	Text(Point(20,130),'5.0K').draw(win)
	Text(Point(20,80),'7.5K').draw(win)
	Text(Point(20,30),'10.0K').draw(win)

        #Draw bar for initial principle

	height=principal*0.02
        bar=Rectangle(Point(40,230),Point(65,230-height))
	bar.setFill("green")
	bar.setWidth(2)
	bar.draw(win)
   
        # bars representing years of interest 


        for year in range(1,11):
            principal=principal*(1+apr)
	    xll=year*25+40
	    height=principal*.02
	    bar = Rectangle(Point(xll,230), Point(xll+25, 230-height))
	    bar.setFill("green")
	    bar.setWidth(2)
	    bar.draw(win)
  
	input("press <enter> to quit")

        win.close()     
 
main()
