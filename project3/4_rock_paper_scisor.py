#!/usr/bin/python
import random 

def play():
	player = input("chose rock(r),scisor(s),paper(p): ")
	me = random.choice(["r","s","p"])

	if player == me:
		return "Oooh it's a tie !! "
	if win(player,me):
		return "you won"

	print("yaaay i won !!!")


def win(p,o):
	if ( p == "r" and o == "s") or ( p == "s" and o == "p") or ( p == "p" and o == "r"):
		return True


print(play())
