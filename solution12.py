with open('input12_4.txt', 'r') as inputFile:
    caveSystem = {}
    for line in inputFile:
        line = line.strip().split('-')
        if line[0] not in caveSystem:
            caveSystem[line[0]] = [line[1]]
        else:
            caveSystem[line[0]].append(line[1])
        if line[1] not in caveSystem:
            caveSystem[line[1]] = [line[0]]
        else:
            caveSystem[line[1]].append(line[0])
    
    unfinishedPaths = [['start']]
    finishedPaths = 0
    
    while len(unfinishedPaths) > 0:
        nextPath = unfinishedPaths.pop(0)
        for adjoiningCave in caveSystem[nextPath[-1]]:
            if adjoiningCave == 'end':
                finishedPaths += 1
            elif str.isupper(adjoiningCave) or adjoiningCave not in nextPath:
                unfinishedPaths.append(nextPath + [adjoiningCave])
    
    print("Number of unique paths that visit small caves no more than once:", finishedPaths)
    
    unfinishedPaths = [['start']]
    finishedPaths = 0
    
    while len(unfinishedPaths) > 0:
        nextPath = unfinishedPaths.pop(0)
        for adjoiningCave in caveSystem[nextPath[-1]]:
            if adjoiningCave == 'end':
                finishedPaths += 1
            elif adjoiningCave == 'start':
                continue
            elif str.isupper(adjoiningCave) or adjoiningCave not in nextPath: 
                unfinishedPaths.append(nextPath + [adjoiningCave])
            else:
                smallCavesInNextPath = [smallCave for smallCave in nextPath if str.islower(smallCave)]
                if len(set(smallCavesInNextPath)) == len(smallCavesInNextPath):
                    unfinishedPaths.append(nextPath + [adjoiningCave])
        
    
    print("Number of unique paths that visit a single small cave twice and all others no more than once:", finishedPaths)
    