with open('input9_2.txt', 'r') as inputFile:
    heightMap = []
    for line in inputFile:
        heightMap.append([int(num) for num in line.strip()])
        
    lowPointCount = 0
    riskLevels = 0
    lowPoints = []
    
    for y in range(len(heightMap)):
        for x in range(len(heightMap[y])):
            if x > 0 and heightMap[y][x - 1] <= heightMap[y][x]:
                continue
            elif x < len(heightMap[y]) - 1 and heightMap[y][x + 1] <= heightMap[y][x]:
                continue
            elif y > 0 and heightMap[y - 1][x] <= heightMap[y][x]:
                continue
            elif y < len(heightMap) - 1 and heightMap[y + 1][x] <= heightMap[y][x]:
                continue
            lowPointCount += 1
            riskLevels += 1 + heightMap[y][x]
            lowPoints.append((y, x))
            
    threeLargest = []
    for lowPoint in lowPoints:
        basinSize = 0
        queue = [lowPoint]
        visited = []
        while len(queue) > 0:
            (y, x) = queue.pop()
            if heightMap[y][x] != 9:
                basinSize += 1
                if y > 0 and (y - 1, x) not in visited and (y - 1, x) not in queue:
                    queue.append((y - 1, x))
                if y < len(heightMap) - 1 and (y + 1, x) not in visited and (y + 1, x) not in queue:
                    queue.append((y + 1, x))
                if x > 0 and (y, x - 1) not in visited and (y, x - 1) not in queue:
                    queue.append((y, x - 1))
                if x < len(heightMap[y]) - 1 and (y, x + 1) not in visited and (y, x + 1) not in queue:
                    queue.append((y, x + 1))
            visited.append((y, x))
        threeLargest.append(basinSize)
        threeLargest.sort(reverse = True)
        threeLargest = threeLargest[:3]
    basinProduct = threeLargest[0] * threeLargest[1] * threeLargest[2]
            
    print("There are {} low points, with a combined risk level count of {}".format(lowPointCount, riskLevels))
    print("The three largest basins are {} with a basin product of {}".format(threeLargest, basinProduct))