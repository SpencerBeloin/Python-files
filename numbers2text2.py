#numbers2text2.py

#this is the decoder



def main():

    print("This program converts a sequence of Unicode numbers into")
    print("The string of text it represents.\n ")



   #get message to encode

    inString=input("Please enter the unicode message to decipher: ")
   
   #loop through subtring and build Unicode message
    chars=[]

    for numStr in inString.split():
        codeNum = eval(numStr)
        chars.append(chr(codeNum))
       


    message = "".join(chars)
    print("\nThe decoded message is:", message)

main()
