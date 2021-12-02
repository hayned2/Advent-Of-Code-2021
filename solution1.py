with open('input1_1.txt', 'r') as inputFile:
    val = int("".join(inputFile.readline().split()))
    if val == None:
        exit()
    newVal = inputFile.readline()
    increases = 0
    while newVal != "":
        if int(val) < int(newVal):
            increases += 1
        val = newVal
        newVal = "".join(inputFile.readline().split())
        if newVal != "":
            newVal = int(newVal)
    print("The number of times that the depth increases is:", increases)
    inputFile.close()
    
with open('input1_1.txt', 'r') as inputFile:
    inputLines = [int("".join(line)) for line in inputFile.readlines()]
    if len(inputLines) < 4:
        exit()
    window1 = None
    window2 = sum(inputLines[0:3])
    x = 1
    increases = 0
    while x < len(inputLines) - 2:
        window1 = window2
        window2 = sum(inputLines[x:x+3])
        x += 1        
        if window1 < window2:
            increases += 1
    print("The number of sliding window increases is:", increases)
    inputFile.close()
        
        

