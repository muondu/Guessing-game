import re
import random

print("Hello, this is a random game. In this game, you will try and guess the number.The numbers will be ranging from 1 - 10")

def logic():	
	a = int(input("Enter your guess: "))
	b = random.randrange(1, 10)
		
	if b == a:
		print("You got it correct")
		print(b)
		
		c = input("Do you want to try again. Please input yes or no:  ")
		
		if not re.match("^[yes,no]*$", c):
			print ("Error! Enter any  below!")
			print(c)
		elif c == "yes":
			logic()
		else:
			print("Goodbye.")
	else:
		print("Try again")
		print(b)
		d = input("Do you give up. Please input yes or no:  ")
		
		if not re.match("^[yes,no]*$", d):
			print ("Error! Enter yes or no below!")
			print(c)
		
		if d == "yes":
			print("Better lack next time.")
		elif d == "no":
			print("You mite guess the write number this time.")
			logic()
logic()