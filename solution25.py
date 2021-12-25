with open('input25_2.txt', 'r') as inputFile:
    board = []
    for line in inputFile:
        line = line.strip()
        board.append(list(line))
    inputFile.close()
    height = len(board)
    width = len(board[0])
    
    #print("Starting board")
    #for line in board:
        #print("".join(line))
    
    changed = True
    step = 0
    while changed:
        changed = False
        easts = set()
        souths = set()
        for y in range(height):
            for x in range(width):
                if board[y][x] == '>':
                    easts.add((y, x))
                elif board[y][x] == 'v':
                    souths.add((y, x))
        
        for (y, x) in easts:
            prospectiveSpot = (x + 1) % width
            if (y, prospectiveSpot) in easts:
                continue
            if board[y][prospectiveSpot] == '.':
                board[y][prospectiveSpot] = '>'
                board[y][x] = '.'
                changed = True
                
        for (y, x) in souths:
            prospectiveSpot = (y + 1) % height
            if (prospectiveSpot, x) in souths:
                continue
            if board[prospectiveSpot][x] == '.':
                board[prospectiveSpot][x] = 'v'
                board[y][x] = '.'
                changed = True
        
        step += 1
        print(step)
        #for line in board:
            #print("".join(line))
        
    print("The board stopped moving on step", step)
    