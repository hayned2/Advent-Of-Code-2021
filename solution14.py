with open('input14_2.txt', 'r') as inputFile:
    pairs = {}
    startingPoint = inputFile.readline().strip()
    for x in range(len(startingPoint) - 1):
        pair = startingPoint[x] + startingPoint[x + 1]
        if pair not in pairs:
            pairs[pair] = 0
        pairs[pair] += 1
    print("Polymer chain starting with:", startingPoint)
    
    inputFile.readline()
    translations = {}
    for line in inputFile:
        line = line.strip().split(' -> ')
        translations[line[0]] = line[1]
    print("Polymer translations:", translations)
    print()
    
    elementCounts = {}   
    for element in set(translations.values()):
        elementCounts[element] = 0    
        
    for element in startingPoint:
        elementCounts[element] += 1
    
    for step in range(40):
        newPairs = {}
        for pair in pairs:
            elementCounts[translations[pair]] += pairs[pair]
            newPair1 = pair[0] + translations[pair]
            newPair2 = translations[pair] + pair[1]
            if newPair1 not in newPairs:
                newPairs[newPair1] = 0
            if newPair2 not in newPairs:
                newPairs[newPair2] = 0
            newPairs[pair[0] + translations[pair]] += pairs[pair]
            newPairs[translations[pair] + pair[1]] += pairs[pair]
        pairs = newPairs
        
        if step in [9, 39]:
            print("Tally of elements at step {}: {}".format(step + 1, elementCounts))
            maxElement = max(elementCounts.values())
            minElement = min(elementCounts.values())
            print("Largest difference between element counts at step {} ({} - {}): {}".format(step + 1, maxElement, minElement, maxElement - minElement))
            print()
