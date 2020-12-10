#!/usr/bin/python
import random

def guess(x):
	low = 0
	high = x 
	feedback = "" # we will use this variable to in/decrement our guess
	guessed = 0 	
	while feedback != "c":
		if low == high:
			guessed = low # same as high because we narrowed the values to one
		else: 
			guessed = random.randint(low,high)
		feedback = input(f"is {guessed} too high(H), too low (L), correct(C): ").lower()
		if feedback == "l":
			low = guessed + 1
		elif feedback == "h":
			high = guessed - 1
	print(" yaaay, i guessed correctly !!!! ")

num = int(input("think of number and don't tell me, and enter a limit for me to guess: "))
guess(num)



