import bisect

class Node:
    
    distance = float("inf")
    
    def __init__(self, position, risk, distance = None):
        self.position = position
        if distance:
            self.distance = distance
        self.risk = risk
        self.neighbors = []
        
    def addNeighbors(self, graph):
        if self.position[0] - 1 >= 0:
            self.neighbors.append((self.position[0] - 1, self.position[1]))
        if self.position[0] + 1 < len(graph[0]):
            self.neighbors.append((self.position[0] + 1, self.position[1]))
        if self.position[1] - 1 >= 0:
            self.neighbors.append((self.position[0], self.position[1] - 1))
        if self.position[1] + 1 < len(graph):
            self.neighbors.append((self.position[0], self.position[1] + 1))
            
    def updateDistance(self, newDistance):
        self.distance = min(self.distance, newDistance + self.risk)
            
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.position[0] == other.position[0] and self.position[1] == other.position[1]
        elif isinstance(other, tuple):
            return self.position[0] == other[0] and self.position[1] == other[1]
        else:
            return False
    
    def __repr__(self):
        return "Node {} - Distance: {} - Risk: {} - Neighbors: {}".format(self.position, self.distance, self.risk, self.neighbors)
    
    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.distance < other.distance
        else:
            return False

with open('input15_2.txt', 'r') as inputFile:
    lines = inputFile.readlines()
    inputFile.close()
    for line in range(len(lines)):
        lines[line] = [int(num) for num in lines[line].strip()]
        
    tiles = (1, 1)
    tileWidth = len(lines[0])
    tileHeight = len(lines)
    
    for y in range(1, tiles[1]):
        for line in range(tileHeight):
            lines.append([num + y if num + y <= 9 else num + y - 9 for num in lines[line]])
            
    for x in range(1, tiles[0]):
        for line in range(len(lines)):
            lines[line] += [num + x if num + x <= 9 else num + x - 9 for num in lines[line][:tileWidth]]
        
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            lines[y][x] = Node((x, y), lines[y][x])
            lines[y][x].addNeighbors(lines)
        
    lines[0][0].distance = 0
    destination = (len(lines[0]) - 1, len(lines) - 1)
    unvisited = [lines[0][0]]
    visited = {}
        
    while True:
        currentNode = unvisited.pop(0)
        if currentNode.position == destination:
            print("Shortest path found! Total risk is:", currentNode.distance)
            break
        visited[currentNode.position] = True
        for neighbor in currentNode.neighbors:
            if neighbor in visited:
                continue
            neighborNode = lines[neighbor[1]][neighbor[0]]
            neighborNode.updateDistance(currentNode.distance)
            if neighborNode not in unvisited:
                bisect.insort_left(unvisited, neighborNode)
        lines[currentNode.position[1]][currentNode.position[0]] = None
    

