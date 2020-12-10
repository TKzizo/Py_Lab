#!/usr/bin/python

import random 

def guess(x):
	random_number = random.randint(1,x)
	guessed = 0
	while random_number != guessed:
		guessed = int(input(f"guess a number between 1 and {x}: "))
		if guessed < random_number:
			print("sorry too low")
		elif guessed > random_number:
			print("oops too high")
	print(f" yes, you guessed right {random_number}")	

rang = int(input("enter range of number to be generated: "))

guess(rang)
