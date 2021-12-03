with open('input3_2.txt', 'r') as inputFile:
    counts = []
    line = inputFile.readline()
    for x in range(len(line.strip())):
        counts.append([0, 0])
    inputFile.seek(0, 0)
    for line in inputFile:
        line = line.strip()
        for x in range(len(line)):
            if line[x] == '1':
                counts[x][1] += 1
            else:
                counts[x][0] += 1
    
    binary = ""
    binary2 = ""
    for count in counts:
        if count[0] > count[1]:
            binary += "0"
            binary2 += "1"
        else:
            binary += "1"
            binary2 += "0"
    
    gamma = int(binary, 2)
    epsilon = int(binary2, 2)
    print("Gamma rate:", gamma, "Epsilon rate:", epsilon, "Multiplied result:", gamma * epsilon)
    
    inputFile.close()

with open('input3_2.txt', 'r') as inputFile:
    values = [line.strip() for line in inputFile.readlines()]
    currentDigit = 0
    while len(values) > 1:
        ones = 0
        zeroes = 0
        for value in values:
            if value[currentDigit] == '1':
                ones += 1
            else:
                zeroes += 1
        
        keptValues = []
        for value in values:
            if ones >= zeroes and value[currentDigit] == '1':
                keptValues.append(value)
            elif ones < zeroes and value[currentDigit] == '0':
                keptValues.append(value)
        values = keptValues
        currentDigit += 1
    
    o2 = int(values[0], 2)
    inputFile.seek(0, 0)
    
    values = [line.strip() for line in inputFile.readlines()]
    currentDigit = 0
    while len(values) > 1:
        ones = 0
        zeroes = 0
        for value in values:
            if value[currentDigit] == '1':
                ones += 1
            else:
                zeroes += 1
        
        keptValues = []
        for value in values:
            if ones >= zeroes and value[currentDigit] == '0':
                keptValues.append(value)
            elif ones < zeroes and value[currentDigit] == '1':
                keptValues.append(value)
        values = keptValues
        currentDigit += 1
        
    co2 = int(values[0], 2)
    print("Oxygen:", o2, "Carbon Dioxide:", co2, "Multiplied result:", o2 * co2)
    inputFile.close()