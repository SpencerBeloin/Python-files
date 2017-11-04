# findmaxoflist.py 

# finds the maximum number of a list of numbers



def main(): 




    n= eval(call(["wc -l numlist.txt"]))


    max = eval(call["head -n1 numlist.txt"])

    

    for i in range(n-1):
        
        x = eval(input(" Enter a number >> "))
        
        if x > max:
            max = x



        print(" the largest value is" , max)

main()
