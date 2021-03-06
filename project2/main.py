import os

def Drawer(board):
	print()
	print(" ---"*9)
	for x in board:
		print(end="| ")
		for y in x:
			for z in y:
				print(z,end=" | ")
		print()
		print(" ---"*9)
	print()

def checkrow(line):
	l = []
	for x in line:
		for y in x:
			l.append(y)
	return len(l) == len(set(l))


def checkcolumn(row):
		
	return len(row) == len(set(row))

def checker(board):
	booleen = True
	row = []
	grid = []
	#checking lines
	for i in board:
		booleen = checkrow(i)
	#cheking column
	for x in range(3):
		for y in range(3):
			for z in range(9):
				row.append(board[z][x][y])
			booleen = checkcolumn(row)
			row = []
	#checkgrid
	beg , end = 0,3
	for a in range(3):
		for _ in range(3):
			for b in range(beg,end):
				grid.append(board[b][a])
			booleen = checkrow(grid)
			grid = []
			beg +=3
			end +=3
		beg = 0
		end = 3 
	print("finished checking \n")
	return booleen

def fill_grid():
	board = []
	line = []
	sub = []
	for i in range(9):
		sentence = "Enter line "+str(i+1)
		while True:
			user = input(sentence)
			if user.isdigit():
				user = list(user)
				for a in range(3):
					sub.append(user[a+2*a])
					sub.append(user[a+2*a+1])
					sub.append(user[a+2*a+2])
					line.append(sub)
					sub = []
				break
			else:
				print("you entered:",user)
				print("please enter digit sequence")
	
		board.append(line)
		line = []
	return board
	
board = [[[0 for x in range(3)] for y in range(3)] for z in range(10)]
Drawer(board)

board = fill_grid()

_ = os.system("clear")
Drawer(board)

if checker(board):
	print("yes, that's correct")
else:
	print("NO, that's not correct")
	
