def calculateDangerZones(includeDiagonals):
    with open('input5_2.txt', 'r') as inputFile:
        hashMap = {}
        for line in inputFile:
            [x1, y1, x2, y2] = [int(num) for num in line.replace(' -> ', ',').strip().split(',')]
            if not includeDiagonals:
                if x1 != x2 and y1 != y2:
                    continue
            dx = dy = 1
            if x2 < x1:
                dx = -1
            if y2 < y1:
                dy = -1
            while True:
                if x1 not in hashMap:
                    hashMap[x1] = {}
                if y1 not in hashMap[x1]:
                    hashMap[x1][y1] = 0
                hashMap[x1][y1] += 1
                
                x1 += dx
                y1 += dy
                
                if y1 - dy == y2 and x1 - dx == x2:
                    break
                elif y1 - dy == y2:
                    y1 = y2
                elif x1 - dx == x2:
                    x1 = x2
        
        dangerZones = 0
        for col in hashMap.keys():
            for row in hashMap[col].keys():
                if hashMap[col][row] >= 2:
                    dangerZones += 1
        print("The number of danger zones with includeDiagonals as", includeDiagonals, "is:", dangerZones)
        
calculateDangerZones(False)
calculateDangerZones(True)