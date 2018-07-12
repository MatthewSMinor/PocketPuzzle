import puzzlefunctions
#python game that resembles the 15 puzzle pocket game
done = False
#making 2d array [3][3]
grid = [[' 1', ' 2', ' 3', ' 4'],[' 5',' 6', ' 7', ' 8'],[' 9', '10', '11', '12'],['-1', '13', '14','15']]

#print the instructions
print('Enter x to exit')

#function to print the contents of the grid
def printGrid():
	for i in range(4):
		print(grid[i])

#initialize position of empty space
markX = 3
markY = 0
choiceX = 0
choiceY = 0

#debug bool
test = False

#making main game loop
while done is False:
	printGrid()
	
	puzzlefunctions.isOnEdge(markX, markY)
	print('The numbers that can move include: '+str(puzzlefunctions.whatCanMove(markX, markY, grid)))
	
	print('Enter a number you would like to move: ')
	choice = input()
	if puzzlefunctions.choiceInWhatCanMove(markX, markY, grid, choice):
		#switch choice with empty space
		for i in range(4):
			for j in range(4):
				if int(choice) == int(grid[i][j]):
					choiceX = i
					choiceY = j
					puzzlefunctions.switch(choiceX, choiceY, markX, markY, grid)
					test = True
					break
			if test is True:
				break
	else:
		print('You cannot move that number')

	test = False

	#changing the markX and y to the right numbers
	markX = choiceX
	markY = choiceY

	
	#ending the game condition
	if input() == 'x':
		done = True

