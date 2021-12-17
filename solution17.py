with open('input17_2.txt', 'r') as inputFile:
    
    line = inputFile.readline().strip().replace("target area: ", "").replace("=", ", ").replace('..', ', ').split(', ')
    inputFile.close()
    
    xMin = int(line[1])
    xMax = int(line[2])
    yMin = int(line[4])
    yMax = int(line[5])
    
    highestHeight = float("-inf")
    stylishTrajectory = []
    successfulTrajectoryCount = 0
    
    for x in range(0, xMax + 1):
        for y in range(yMin, -yMin):
            
            trajectory = [x, y]
            position = [0, 0]
            trajectoryMax = float("-inf")
            
            while position[0] <= xMax and position[1] >= yMin:
                
                position = [position[0] + trajectory[0], position[1] + trajectory[1]]
                trajectoryMax = max(trajectoryMax, position[1])
                
                if position[0] >= xMin and position[0] <= xMax and position[1] >= yMin and position[1] <= yMax:
                    successfulTrajectoryCount += 1
                    if trajectoryMax > highestHeight:
                        highestHeight = trajectoryMax
                        stylishTrajectory = [x, y]
                    break
                
                if trajectory[0] < 0:
                    trajectory[0] += 1
                elif trajectory[0] > 0:
                    trajectory[0] -= 1
                trajectory[1] -= 1
                
    print("The most stylish trajectory is {}, with a maximum height of {}".format(stylishTrajectory, highestHeight))
    print("There are a total of {} trajectories that will successfully land the probe in the target area".format(successfulTrajectoryCount))
        