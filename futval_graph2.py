#futval_graph3.py
from graphics import * 


def drawBar(window, year, height):
    #draw a bar in window starting at year with given height
    bar = Rectangle(Point(year,0), Point(year+1, height))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(window)


def main():
    #Introduction 
    print("This program plots the growth of a 10-yr investement")
    

    #ask for principal and interest rate 
    
    principal=eval(input("Enter the initial principal: "))
    apr=eval(input("Enter the annualized interest rate: "))


    # Creat a graphics window with labels on left edge
    win = GraphWin("Investment Growth Chart", 320, 240)
    win.setCoords(-1.75,-200,11.5,10400)
    Text(Point(-1,0), '0.0K').draw(win)
    Text(Point(-1,2500), '2.5K').draw(win)
    Text(Point(-1,5000), '5.0K').draw(win)
    Text(Point(-1,7500), '7.5K').draw(win)
    Text(Point(-1,10000), '10.0K').draw(win)
    


    drawBar(win,0,principal)
    for year in range(1,11):
        principal = principal * ( 1 + apr)
        drawBar(win,year,principal)
        

    input("press <enter> to quit. ")
    win.close()

main()
