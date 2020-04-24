import random

print("Hello, this is a random game. In this game, you will try and gess the number.The numbers will be ranging from 1 - 10")

def logic():	
	a = int(input("Enter your gess: "))
	b = random.randrange(1, 10)
		
	if b == a:
		print("You got it correct")
		print(b)
	else:
		print("Try again")
		print(b)
		logic()
logic()