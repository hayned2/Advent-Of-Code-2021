# Search the board for the number and replace it with -1 if found
def newNumber(num, board):
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] == num:
                board[x][y] = -1
                return board
    return board

# Check for a column or row of only -1
def checkForWin(board):
    for x in range(len(board)):
        if board[x] == [-1] * len(board[x]):
            return True
    
    for x in range(len(board[0])):
        col = []
        for y in range(len(board)):
            col.append(board[y][x])
        if col == [-1] * len(board[x]):
            return True
    return False
      
# Calculate the sum of the numbers in the board that are not -1 times the winning number  
def calculateScore(winningNumber, board):
    total = 0
    for row in board:
        for col in row:
            if col != -1:
                total += int(col)
    return total * int(winningNumber)

with open('input4_2.txt', 'r') as inputFile:
    
    # Get the numbers that are called.
    inputs = inputFile.readline().strip().split(',')
    print(inputs)
    
    # Create a 2D array for each board, which we know are 5x5
    boards = []
    for line in inputFile:
        while len(line.strip()) == 0:
            line = inputFile.readline()
        currentBoard = []
        currentBoard.append(line.split())
        for x in range(4):
            line = inputFile.readline().split()
            currentBoard.append(line)
        boards.append(currentBoard)
    
    inputFile.close()
    
    # Go through each called number
    for num in inputs:
        for x in range(len(boards)):
            
            # Boards are marked as None once they win
            if boards[x] == None:
                continue
            
            # Mark the number off if it's in the board
            boards[x] = newNumber(num, boards[x])
            
            # Check for a winning board, declare it if we have it and mark it as None
            if checkForWin(boards[x]):
                print("Winning board!", boards[x])
                print("Winning number:", num, "Winning score:", calculateScore(num, boards[x]))
                boards[x] = None
                
            # Check if we've marked off all of the boards
            if boards == [None] * len(boards):
                print("All boards gone!")
                exit()