def add(num1, num2):
    return reduce('[{},{}]'.format(num1, num2))

def explode(num):
    nests = 0
    previousNum = -1
    previousNumLength = 0
    nextNum = -1
    nextNumLength = 0
    first = -1
    firstLength = 0
    second = -1
    secondLength = 0
    x = 0
    while x < len(num):
        if first == -1:
            if num[x] == '[':
                nests += 1
            elif num[x] == ']':
                nests -= 1
            elif num[x].isdigit():
                if nests >= 5:
                    first = x
                    firstLength = 1
                    while num[x + 1].isdigit():
                        firstLength += 1
                        x += 1
                    if not num[x + 2].isdigit():
                        first = -1
                        firstLength = 0
                        x += 1
                        continue
                    x += 2
                    second = x
                    secondLength = 1
                    while num[x + 1].isdigit():
                        secondLength += 1
                        x += 1
                else:
                    if x == previousNum + previousNumLength:
                        previousNumLength += 1
                    else:
                        previousNum = x
                        previousNumLength = 1
        else:
            if num[x].isdigit():
                nextNum = x
                nextNumLength = 1
                while num[x + 1].isdigit():
                    nextNumLength += 1
                    x += 1
                break
        x += 1
    
    if firstLength == 0:
        return num
    
    prefix = num[:first - 1]
    suffix = num[second + secondLength + 1:]
    
    if nextNumLength > 0:
        newNext = str(int(num[nextNum : nextNum + nextNumLength]) + int(num[second : second + secondLength]))
        suffix = num[second + secondLength + 1 : nextNum] + newNext + num[nextNum + nextNumLength:]
    
    if previousNumLength > 0:
        newPrevious = str(int(num[previousNum : previousNum + previousNumLength]) + int(num[first : first + firstLength]))
        prefix = num[:previousNum] + newPrevious + num[previousNum + previousNumLength : first - 1]
    
    return prefix + '0' + suffix

def split(num):
    currentNum = -1
    currentNumString = ''
    x = 0
    while x < len(num):
        if num[x].isdigit():
            if x == currentNum + 1:
                currentNumString += num[x]
            else:
                currentNum = x
                currentNumString = num[x]
        elif len(currentNumString) > 1:
            break
        x += 1
    
    if len(currentNumString) > 1:
        roundedDown = int(currentNumString) // 2
        roundedUp = -(int(currentNumString) // -2)
        return num[:currentNum] + "[{},{}]".format(roundedDown, roundedUp) + num[currentNum + len(currentNumString):]
    else:
        return num
            
def reduce(num):
    newNum = explode(num)
    if newNum != num:
        return reduce(newNum)
    newNum = split(num)
    if newNum != num:
        return reduce(newNum)
    return num
    
def magnitude(num):
    x = 0
    first = -1
    firstString = ''
    second = -1
    secondString = ''
    while num[0] == '[':
        if num[x].isdigit():
            first = x
            firstString = num[x]
            while num[x + 1].isdigit():
                firstString += num[x + 1]
                x += 1
            if num[x + 1] != ',':
                continue
            x += 2
            if x < len(num) and num[x].isdigit():
                second = x
                secondString = num[x]
                while num[x + 1].isdigit():
                    secondString += num[x + 1]
                    x += 1
                num = num[:first - 1] + str((3 * int(firstString)) + (2 * int(secondString))) + num[second + len(secondString) + 1:]
                x = -1
        x += 1
    return int(num)
        
        

with open('input18_3.txt', 'r') as inputFile:
    lines = [line.strip() for line in inputFile.readlines()]
    inputFile.close()
    linesCopy = lines[:]
    while len(lines) > 1:
        newSum = add(lines.pop(0), lines.pop(0))
        lines = [newSum] + lines
    print("The final sum is {}, with a magnitude of {}".format(lines[0], magnitude(lines[0])))
    
    maxMagnitude = float("-inf")
    maxMagnitudeValues = []
    for num1 in linesCopy:
        for num2 in linesCopy:
            if num1 == num2:
                continue
            numSum = add(num1, num2)
            numMagnitude = magnitude(numSum)
            if numMagnitude > maxMagnitude:
                maxMagnitude = numMagnitude
                maxMagnitudeValues = [num1, num2, numSum]
    
    print("The numbers {} and {} sum together to {}, with the highest magnitude of {}".format(maxMagnitudeValues[0], maxMagnitudeValues[1], maxMagnitudeValues[2], maxMagnitude))

