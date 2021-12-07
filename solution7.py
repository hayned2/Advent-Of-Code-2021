with open('input7_2.txt', 'r') as inputFile:
    
    # Get the numbers that are called.
    inputs = [int(num) for num in inputFile.readline().strip().split(',')]
    
    hashMap = {}
    for position in inputs:
        if position not in hashMap:
            hashMap[position] = 1
        else:
            hashMap[position] += 1
                
    lowestCost = float('inf')
    lowestAlignment = None
    lowestExpCost = float('inf')
    lowestExpAlignment = None
    for proposedAlignment in range(0, max(hashMap)):
        currentCost = 0
        currentExpCost = 0
        for position in hashMap:
            distance = abs(proposedAlignment - position)
            currentCost += hashMap[position] * (distance)
            currentExpCost += int(hashMap[position] * (distance * (distance + 1) / 2))
        if currentCost < lowestCost:
            lowestCost = currentCost
            lowestAlignment = proposedAlignment
        if currentExpCost < lowestExpCost:
            lowestExpCost = currentExpCost
            lowestExpAlignment = proposedAlignment
    
    print("The best position for the crabs is position {}, with a linear fuel cost of {}".format(lowestAlignment, lowestCost))
    print("The best position for the crabs is position {}, with an exponential fuel cost of {}".format(lowestExpAlignment, lowestExpCost))
        