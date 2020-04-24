import random

print("Hello, this is a random game. In this game, you will try and gess the number.The numbers will be ranging from 1 - 10")

def logic():	
	a = int(input("Enter your gess: "))
	b = random.randrange(1, 10)
		
	if b == a:
		print("You got it correct")
		print(b)
		
		c = input("Do you want to try again. Please input yes or no:  ")
		if c == "yes":
			logic()
		else:
			print("Goodbye.")
	else:
		print("Try again")
		print(b)
		d = input("Do you give up. Please input yes or no:  ")
		if d == "yes":
			print("Better lack next time.")
		elif d == "no":
			print("You mite gess the write number this time.")
			logic()
logic()