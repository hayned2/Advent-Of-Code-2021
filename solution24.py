from math import trunc

with open('input24_1.txt', 'r') as inputFile:
    lines = [line.strip().split(" ") for line in inputFile.readlines()]
    inputFile.close()
    testNumber = 13579246899999
    while True:
        variables = {
            'w': 0,
            'x': 0,
            'y': 0,
            'z': 0
        }
        testNumber2 = str(testNumber)
        for line in lines:
            if line[0] == 'inp':
                print(variables)
                variables[line[1]] = int(testNumber2[0])
                testNumber2 = testNumber2[1:]
            elif line[0] == 'add':
                if line[2].replace('-', '').isdigit():
                    variables[line[1]] += int(line[2])
                else:
                    variables[line[1]] += variables[line[2]]
            elif line[0] == 'mul':
                if line[2].replace('-', '').isdigit():
                    variables[line[1]] *= int(line[2])
                else:
                    variables[line[1]] *= variables[line[2]]
            elif line[0] == 'div':
                if line[2].replace('-', '').isdigit():
                    variables[line[1]] = trunc(variables[line[1]] / int(line[2]))
                else:
                    variables[line[1]] = trunc(variables[line[1]] / variables[line[2]])                    
            elif line[0] == 'mod':
                if line[2].replace('-', '').isdigit():
                    variables[line[1]] = variables[line[1]] % int(line[2])
                else:
                    variables[line[1]] = variables[line[1]] % variables[line[2]]                    
            elif line[0] == 'eql':
                if line[2].replace('-', '').isdigit():
                    variables[line[1]] = int(variables[line[1]] == int(line[2]))
                else:
                    variables[line[1]] = int(variables[line[1]] == variables[line[2]])                    
        print(variables, "Final result")
        if variables['z'] == 0:
            print("The largest accepted MONAD is", testNumber)
            exit()
        else:
            print("Not a valid serial number")
            exit()
            testNumber -= 1