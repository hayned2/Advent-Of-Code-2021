with open('input13_2.txt', 'r') as inputFile:
    folds = False
    dots = []
    for line in inputFile:
        line = line.strip()
        if line == "":
            folds = True
            print("Total number of dots before folding:", len(dots))
            continue
        if not folds:
            line = [int(num) for num in line.split(',')]
            dots.append(tuple(line))
        else:
            [axis, foldLine] = line.split()[2:][0].split('=')
            foldLine = int(foldLine)
            for d in range(len(dots)):
                if axis == 'x' and dots[d][0] > foldLine:
                    dots[d] = (foldLine - abs(foldLine - dots[d][0]), dots[d][1])
                elif axis == 'y' and dots[d][1] > foldLine:
                    dots[d] = (dots[d][0], foldLine - abs(foldLine - dots[d][1]))
            dots = list(set(dots))
            print("Total number of dots after folding along {} axis on line {}: {}".format(axis, foldLine, len(dots)))
            
    maxX = maxY = -1
    for dot in dots:
        maxX = max(maxX, dot[0])
        maxY = max(maxY, dot[1])
    grid = []
    for y in range(maxY + 1):
        row = []
        for x in range(maxX + 1):
            row.append(' ')
        grid.append(row)
    for dot in dots:
        grid[dot[1]][dot[0]] = '#'
    for row in grid:
        print("".join(row))
                
            