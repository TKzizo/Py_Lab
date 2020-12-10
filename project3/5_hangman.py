#!/usr/bin/python


import string 
# get a new word list 


def valid_word():
	word = # select from the word list
	while "-" in word or " " in word:
		word = # select from word list 
	return word 

def hangman(x):
	word = x
	word_letters = set(x)
	alphabet = set(string.ascii_uppercase)
	used_letters = set() # already guessed letters 

	while len(word_letters > 0):

		print("Used letter: ", " ".join(used_letters))
		word_list = [letter if letter in used_letters else "-" for letter in word]
		print(" ".join(used_letters))

		user_letter = input("guess a letter: ")
		if user_letter in alphabet - used_letters:
			used_letters.add(user_letter)
			if user_letter in word_letters:
				word_letter.remove(user_letter)
		elif user_letter in used_letter:
			print("you already used that letter ")
		else: 
			print("that's invalid character")
		

hangman(valid_word())

