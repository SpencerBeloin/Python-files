#printfile.py 

# prints hello.txt


def main():

    fname=input("Enter filename: " )
    infile = open(fname, "r")
    data= infile.read()
    print(data)

main()
