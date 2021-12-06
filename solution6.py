with open('input6_2.txt', 'r') as inputFile:
    
    school = {}
    for x in range(9):
        school[x] = 0
    
    fish = [int(num) for num in inputFile.readline().strip().split(',')]
    for fishy in fish:
        school[fishy] += 1
        
    inputFile.close()
    
    for day in range(256):
        birthingFish = school[0]
        for x in range(1, 9):
            school[x - 1] = school[x]
        school[6] += birthingFish
        school[8] = birthingFish
        if day == 79 or day == 255:
            population = 0
            for ages in school:
                population += school[ages]
                
            print("The fish population in {} days is: {}".format(day + 1, population))
