class Cube:
    def __init__(self, bounds, on):
        self.on = on
        self.xMin = bounds[0]
        self.xMax = bounds[1]
        self.yMin = bounds[2]
        self.yMax = bounds[3]
        self.zMin = bounds[4]
        self.zMax = bounds[5]
        
    def getBounds(self):
        return [self.xMin, self.xMax, self.yMin, self.yMax, self.zMin, self.zMax]
    
    def getVolume(self):
        return (self.xMax - self.xMin) * (self.yMax - self.yMin) * (self.zMax - self.zMin)
    
    def __repr__(self):
        return "Cube ({}, {}, {}) to ({}, {}, {}) Size {}".format(self.xMin, self.yMin, self.zMin, self.xMax, self.yMax, self.zMax, self.getVolume())

with open('input22_2.txt', 'r') as inputFile:
    cubes = {}    
    for line in inputFile:
        line = line.strip()
        line = line.split(" ")
        on = (line[0] == "on")
        line = [int(l[2:]) if "=" in l else int(l) for l in line[1].replace("..", ",").split(",")]
        if max([abs(value) for value in line]) > 50:
            print("After all initialization steps, there are a total of {} cubes turned on".format(len(cubes)))
            break
        for x in range(line[0], line[1] + 1):
            for y in range(line[2], line[3] + 1):
                for z in range(line[4], line[5] + 1):
                    if on:
                        cubes[(x, y, z)] = True
                    elif (x, y, z) in cubes:
                        cubes.pop((x, y, z))
                    
with open('input22_2.txt', 'r') as inputFile:
    cubes = []
    for line in inputFile:
        line = line.strip()
        line = line.split(" ")
        on = (line[0] == "on")
        line = [int(l[2:]) if "=" in l else int(l) + 1 for l in line[1].replace("..", ",").split(",")]
        newCube = Cube(line, on)
        newCubes = []
        for n in range(len(cubes)):
            
            if not (newCube.xMax > cubes[n].xMin and newCube.xMin < cubes[n].xMax \
                and newCube.yMax > cubes[n].yMin and newCube.yMin < cubes[n].yMax \
                and newCube.zMax > cubes[n].zMin and newCube.zMin < cubes[n].zMax):
                newCubes.append(cubes[n])
                continue
            
            
            if cubes[n].xMax > newCube.xMax:
                newerCube = Cube(cubes[n].getBounds(), cubes[n].on)
                newerCube.xMin = newCube.xMax
                newCubes.append(newerCube)
                cubes[n].xMax = newCube.xMax
                
            if cubes[n].xMin < newCube.xMin:
                newerCube = Cube(cubes[n].getBounds(), cubes[n].on)
                newerCube.xMax = newCube.xMin
                newCubes.append(newerCube)
                cubes[n].xMin = newCube.xMin
            
            if cubes[n].yMax > newCube.yMax:
                newerCube = Cube(cubes[n].getBounds(), cubes[n].on)
                newerCube.yMin = newCube.yMax
                newCubes.append(newerCube)
                cubes[n].yMax = newCube.yMax
                
            if cubes[n].yMin < newCube.yMin:
                newerCube = Cube(cubes[n].getBounds(), cubes[n].on)
                newerCube.yMax = newCube.yMin
                newCubes.append(newerCube)
                cubes[n].yMin = newCube.yMin
                
            if cubes[n].zMax > newCube.zMax:
                newerCube = Cube(cubes[n].getBounds(), cubes[n].on)
                newerCube.zMin = newCube.zMax
                newCubes.append(newerCube)
                cubes[n].zMax = newCube.zMax
                
            if cubes[n].zMin < newCube.zMin:
                newerCube = Cube(cubes[n].getBounds(), cubes[n].on)
                newerCube.zMax = newCube.zMin
                newCubes.append(newerCube)
                cubes[n].zMin = newCube.zMin
            
                
        newCubes.append(newCube)
        cubes = newCubes
        
    totalCubes = 0
    for cube in cubes:
        if cube.on:
            totalCubes += cube.getVolume()
    print("After all reboot steps, there are a total of {} cubes turned on".format(totalCubes))
    
    
    