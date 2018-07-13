import random


#check if empty space is on an edge
def isOnEdge(markX, markY):
	if markX > 0 and markX < 3 and markY > 0 and markY < 3:
		return False
	else:
		return True
#find numbers that are eligable to use
def whatCanMove(markX, markY, grid):
	canMoveUp = True
	canMoveDown = True
	canMoveLeft = True
	canMoveRight = True
	numbersThatCanMove = []
	#determine which ways you can move from the empty mark
	if isOnEdge(markX, markY):
		#find out what edge
		if markX == 0:
			canMoveUp = False
		if markX == 3:
			canMoveDown = False
		if markY == 0:
			canMoveLeft = False
		if markY == 3:
			canMoveRight = False

	#check available slots and see what number is in them
	if canMoveUp:
		numbersThatCanMove.append(grid[markX-1][markY])
	if canMoveDown:
		numbersThatCanMove.append(grid[markX+1][markY])
	if canMoveLeft:
		numbersThatCanMove.append(grid[markX][markY-1])
	if canMoveRight:
		numbersThatCanMove.append(grid[markX][markY+1])

	#return the list of numbers that can move
	return numbersThatCanMove


def choiceInWhatCanMove(markX, markY, grid, choice):
	avail = whatCanMove(markX, markY, grid)
	for thing in avail:
		if int(choice) == int(thing):
			return True

#changing the location of the empty space with that of the choice and viceversa
def switch(choiceX, choiceY, markX, markY, grid):
	tempChoice = grid[choiceX][choiceY]
	tempMark = grid[markX][markY]
	grid[choiceX][choiceY] = tempMark
	grid[markX][markY] = tempChoice

#populate the grid with random numbers w/out repeat 1 - 15 and include -1 for empty space
def popGrid():
	grid = []
	grid.append([])
	grid.append([])
	grid.append([])
	grid.append([])

	nums = [' 1', ' 2', ' 3', ' 4', ' 5', ' 6', ' 7', ' 8', ' 9', '10', '11', '12', '13', '14', '15', '-1']
	count = len(nums)

	for i in range(4):
		for j in range(4):
			count = count -1
			r = random.randint(0, count)
			grid[i].append(nums[r])
			nums.remove(nums[r])
			
	return grid

#check if the player has won
def checkWin(grid):
	winLayout = [[' 1', ' 2', ' 3', ' 4'],[' 5', ' 6', ' 7', ' 8'],[' 9', '10', '11', '12'],['13', '14', '15', '-1', ]]
	for i in range(4):
		for j in range(4):
			if grid == winLayout:
				return True