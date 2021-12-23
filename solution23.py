import copy

hallwayPositions = [0, 1, 3, 5, 7, 9, 10]
roomPositions = [2, 4, 6, 8]
energyCosts = {
    "A": 1,
    "B": 10,
    "C": 100,
    "D": 1000
}


class Room:
    def __init__(self, spot, inhabitants):
        self.spot = spot
        self.inhabitants = inhabitants
    
    def __repr__(self):
        return "Room {}: ({})".format(self.spot, ", ".join(self.inhabitants))
    
    def canMoveIn(self):
        return all([(inhabitant == self.spot or inhabitant == '.') for inhabitant in self.inhabitants])
    
    def moveIn(self):
        for x in range(len(self.inhabitants) - 1, -1, -1):
            if self.inhabitants[x] == '.':
                self.inhabitants[x] = self.spot
                return x + 1
            
    def isSorted(self):
        return all([inhabitant == self.spot for inhabitant in self.inhabitants])
    
    def isEmpty(self):
        return all([inhabitant == '.' for inhabitant in self.inhabitants])
    
    def moveOut(self):
        for x in range(len(self.inhabitants)):
            if self.inhabitants[x] != '.':
                tenant = self.inhabitants[x]
                self.inhabitants[x] = '.'
                return (tenant, x + 1)

# Given a position in the hallway, return which rooms can be entered without being blocked
def getReachableRooms(startingPosition, hallway):
    if startingPosition == 0 and hallway[1] != '.':
        return []
    if startingPosition == len and hallway[5] != '.':
        return []
    rooms = []
    for x in roomPositions:
        if startingPosition < x:
            if all([spot == '.' for spot in hallway[startingPosition + 1 : x]]):
                rooms.append(((x // 2) - 1, x - startingPosition))
        else:
            if all([spot == '.' for spot in hallway[x : startingPosition]]):
                rooms.append(((x // 2) - 1, startingPosition - x))
    return rooms

# Given a room, return which positions in the hallway can be entered without being blocked
def getReachableHallways(startingRoom, hallway):
    hallways = []
    for x in hallwayPositions:
        if startingRoom < x:
            if all([spot == '.' for spot in hallway[startingRoom + 1 : x + 1]]):
                hallways.append((x, x - startingRoom))
        else:
            if all([spot == '.' for spot in hallway[x : startingRoom]]):
                hallways.append((x, startingRoom - x))
    return hallways

# Return the state of the hallway and rooms as a string to store in a hash
# This way we can track which states we've already seen and can skip
def getState(hallway, rooms):
    state = "".join(hallway)
    for room in rooms:
        state += "".join(room.inhabitants)
    return state


# The primary solving function
def sortAmphipods(hallway, rooms, totalCost):

    # We track all of the future states of the board
    nextMoves = [(totalCost, hallway, rooms, [])]
    visitedStates = {}
    
    # Keep going while there are states to explore
    while len(nextMoves) > 0:
        
        # Get the next move, skip it if it's a state we've seen previously
        (currentCost, currentHallway, currentRooms, previousMoves) = nextMoves.pop(0)
        state = getState(currentHallway, currentRooms)
        if state in visitedStates:
            continue
        else:
            visitedStates[state] = True
        
        # Check to see if this is the fully sorted state
        if all([room.isSorted() for room in currentRooms]):
            print("The shortest path has been found!")
            for move in previousMoves:
                print(move)
            print("Total cost:", currentCost)
            return currentCost
    
        # See if any in the hallways can move into their appropriate rooms
        for h in hallwayPositions:
            if currentHallway[h] == '.':
                continue
            for (room, cost) in getReachableRooms(h, currentHallway):
                if currentRooms[room].spot != currentHallway[h]:
                    continue
                if not currentRooms[room].isSorted() and currentRooms[room].canMoveIn():
                    roomsCopy = copy.deepcopy(currentRooms)
                    cost += roomsCopy[room].moveIn()
                    cost *= energyCosts[currentHallway[h]]
                    hallwayCopy = currentHallway[:]
                    hallwayCopy[h] = '.'
                    nextMoves.append((currentCost + cost, hallwayCopy, roomsCopy, previousMoves + ["Moved {} from hallway {} to room {} for cost of {}".format(currentHallway[h], h, currentRooms[room].spot, cost)]))
                
        # See if any in the rooms can move to the hallways
        for index, roomPosition in enumerate(roomPositions):
            if currentRooms[index].isSorted() or currentRooms[index].canMoveIn():
                continue
            for (hall, cost) in getReachableHallways(roomPosition, currentHallway):
                roomsCopy = copy.deepcopy(currentRooms)
                hallwayCopy = currentHallway[:]
                (leaver, extraCost) = roomsCopy[index].moveOut()
                hallwayCopy[hall] = leaver
                cost += extraCost
                cost *= energyCosts[leaver]
                nextMoves.append((currentCost + cost, hallwayCopy, roomsCopy, previousMoves + ["Moved {} from room {} to hallway {} for cost of {}".format(leaver, currentRooms[index].spot, hall, cost)]))

        # Sort the next moves by cost, so that the next move is the one with the lowest cost
        nextMoves.sort(key = lambda x : x[0])
        
    return float("inf")
        

with open('input23_4.txt', 'r') as inputFile:
    lines = [line.strip() for line in inputFile.readlines()]
    inputFile.close()
    amphipods = [line.replace('#', '') for line in lines[2:-1]]
    hallway = ['.'] * (len(lines[1]) - 2)
    rooms = []
    for x in range(4):
        inhabitants = []
        for y in range(len(amphipods)):
            inhabitants.append(amphipods[y][x])
        room = Room(chr(ord('A') + x), inhabitants)
        rooms.append(room)
        
    print(hallway)
    print(rooms)
    
    sortAmphipods(hallway, rooms, 0)
    
    