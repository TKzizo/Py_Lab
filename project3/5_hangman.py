#!/usr/bin/python

import string 
import random
from words import listofwords

def valid_word():
	word = random.choice(listofwords).upper()
	while ("-" in word) or (" " in word):
		word = random.choice(listofwords)
	return word 

def hangman(x):
	word = x
	word_letters = set(x)	
	alphabet = set(string.ascii_uppercase)
	used_letters = set() 

	while len(word_letters) > 0:

		print("Used letter: ", " ".join(used_letters))
		word_list = [letter if letter in used_letters else "-" for letter in word]
		print("current word: "," ".join(word_list))

		user_letter = input("guess a letter: ")
		if (user_letter in alphabet - used_letters):
			used_letters.add(user_letter)
			if (user_letter in word_letters):
				word_letters.remove(user_letter)
		elif (user_letter in used_letters):
			print("you already used that letter ")
		else: 
			print("that's invalid character")
	print("Congrats you found the word !!!!")
	input()	
	
hangman(valid_word())
