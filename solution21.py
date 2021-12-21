class Player:
    def __init__(self, number, position):
        self.score = 0
        self.number = number
        self.position = position
        
    def takeTurn(self, deterministicDie):
        rolls = []
        for x in range(3):
            if deterministicDie == 101:
                deterministicDie = 1
            rolls.append(deterministicDie)
            deterministicDie += 1
        self.position = (self.position + sum(rolls)) % 10
        if self.position == 0:
            self.position = 10
        self.score += self.position
        #print("Player {} rolls {} and moves to space {} for a total score of {}.".format(self.number, "+".join([str(roll) for roll in rolls]), self.position, self.score))
        return deterministicDie
        
    def __repr__(self):
        return "Player {} is at position {} with a score of {}".format(self.number, self.position, self.score)
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.number == other.number and self.position == other.position and self.score == other.score            

with open('input21_1.txt', 'r') as inputFile:
    player1 = Player(1, int(inputFile.readline().strip().split()[-1]))
    player2 = Player(2, int(inputFile.readline().strip().split()[-1]))
    
    deterministicDie = 1
    currentTurn = 0
    diceRolls = 0
    while player1.score < 1000 and player2.score < 1000:
        if currentTurn == 0:
            deterministicDie = player1.takeTurn(deterministicDie)
        else:
            deterministicDie = player2.takeTurn(deterministicDie)
        diceRolls += 3
        currentTurn = (currentTurn + 1) % 2
    
    losingScore = min(player1.score, player2.score)
    print("Deterministic Die Game")
    print("The losing player's score ({}) times the number of dice rolls ({}) is {}\n".format(losingScore, diceRolls, losingScore * diceRolls))
    
    
def determineQuanticResults(state):
    quanticResults = []
    for x in range(1, 4):
        for y in range(1, 4):
            for z in range(1, 4):
                if state[2] == 0:
                    newPosition = (state[0][0] + x + y + z) % 10
                    if newPosition == 0:
                        newPosition = 10
                    newScore = state[0][1] + newPosition
                    quanticResults.append(((newPosition, newScore), state[1], 1))
                else:
                    newPosition = (state[1][0] + x + y + z) % 10
                    if newPosition == 0:
                        newPosition = 10
                    newScore = state[1][1] + newPosition
                    quanticResults.append((state[0], (newPosition, newScore), 0))
    return quanticResults
            
with open('input21_2.txt', 'r') as inputFile:
    player1Position = int(inputFile.readline().strip().split()[-1])
    player2Position = int(inputFile.readline().strip().split()[-1])
    universes = {((player1Position, 0), (player2Position, 0), 0): 1}
    
    player1Victories = 0
    player2Victories = 0
    while len(universes) > 0:
        newUniverses = {}
        for state in universes:
            quanticResults = determineQuanticResults(state)
            for result in quanticResults:
                if result[0][1] >= 21:
                    player1Victories += universes[state]
                elif result[1][1] >= 21:
                    player2Victories += universes[state]
                else:
                    if result not in newUniverses:
                        newUniverses[result] = 0
                    newUniverses[result] += universes[state]
        universes = newUniverses
    
    print("Quantum Die Game")
    print("Player 1 won in {} universes and Player 2 won in {} universes".format(player1Victories, player2Victories))
    