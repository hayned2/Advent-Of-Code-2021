with open('input2_2.txt', 'r') as inputFile:
    horizontal = 0
    depth = 0
    for line in inputFile:
        direction, distance = line.split()
        if direction == 'forward':
            horizontal += int(distance)
        elif direction == 'down':
            depth += int(distance)
        elif direction == 'up':
            depth -= int(distance)
    result = horizontal * depth
    print("Multiplied distance is:", result)
    inputFile.close()
    
with open('input2_2.txt', 'r') as inputFile:
    horizontal = 0
    depth = 0
    aim = 0
    for line in inputFile:
        direction, distance = line.split()
        if direction == 'forward':
            horizontal += int(distance)
            depth += aim * int(distance)
        elif direction == 'down':
            aim += int(distance)
        elif direction == 'up':
            aim -= int(distance)
    result = horizontal * depth
    print("Aimed distance is:", result)
    inputFile.close()