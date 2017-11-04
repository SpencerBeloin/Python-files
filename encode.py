#encode.py
#encoding with 7 bit UNICODE


import sys 

def main():

	print("This program will convert a message into Unicode encoding  \n")

	message = input("Please enter the message to encode: ")


	print("\n Here are the unicode codes:  ")


	for ch in message:
		print(ord(ch)),


main()	
