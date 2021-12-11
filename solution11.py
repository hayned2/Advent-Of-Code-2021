class DumboOctopus:
    energyLevel = -1
    flashed = False
    neighbors = []
    position = -1
    
    def __init__(self, energy, position):
        self.energyLevel = int(energy)
        self.position = position
        
    def increaseEnergy(self):
        if self.flashed:
            return False
        self.energyLevel += 1
        if self.energyLevel > 9:
            self.energyLevel = 0
            self.flashed = True
        return self.flashed
            
    def resetFlash(self):
        self.flashed = False
        
    def setNeighbors(self, neighbors):
        self.neighbors = neighbors

with open('input11_2.txt', 'r') as inputFile:
    
    octopi = []
    
    lines = inputFile.readlines()
    inputFile.close()
    height = len(lines)
    width = len(lines[0].strip())
    total = height * width
    
    # Create a 2D array of DumboOctopus class objects
    for line in range(height):
        row = []
        for octopus in range(width):
            row.append(DumboOctopus(lines[line][octopus], octopus))
        octopi.append(row)
            
    # Each octopus keeps track of its neighbors so we don't have to
    for y in range(height):
        for x in range(width):
            neighbors = []
            for y2 in range(max(0, y - 1), min(height, y + 2)):
                for x2 in range(max(0, x - 1), min(width, x + 2)):
                    if y2 == y and x2 == x:
                        continue
                    neighbors.append((y2, x2))
            octopi[y][x].setNeighbors(neighbors)
                
    totalFlashes = 0
    step = 0
    
    # Keep going until all of the octopi flash at the same time
    while True:
        stepFlashes = 0
        chainReaction = []
        
        # Increase the energy for each octopus
        for y in range(height):
            for x in range(width):
                chainReaction.append((y, x))
        
        # Keep increasing energy for each octopus until the step is complete
        while len(chainReaction) > 0:
            octopus = chainReaction.pop()
            if octopi[octopus[0]][octopus[1]].increaseEnergy():
                stepFlashes += 1
                for neighbor in octopi[octopus[0]][octopus[1]].neighbors:
                    if not octopi[neighbor[0]][neighbor[1]].flashed:
                        chainReaction.append(neighbor)
                    
        # Reset the octopi that flashed so they can flash again on the next step
        for y in range(height):
            for x in range(width):
                octopi[y][x].resetFlash()
                
        totalFlashes += stepFlashes
        step += 1
        print("Step {}: {} total flashes".format(step, totalFlashes))
        
        if stepFlashes == total:
            print("Simultaneous flashing has occurred at step {}".format(step))
            break