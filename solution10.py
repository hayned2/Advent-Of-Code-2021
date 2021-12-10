with open('input10_2.txt', 'r') as inputFile:
    
    openers = '{(<['
    closers = '})>]'
    scoreTable = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
        "(": 1,
        "[": 2,
        "{": 3,
        "<": 4
    }
    
    syntaxErrorScore = 0
    autoCompletionScores = []
    
    for line in inputFile:
        line = line.strip()
        pending = ''
        corrupted = False
        for character in line:
            if character in openers:
                pending += character
            elif character in closers:
                if (character == '}' and pending[-1] != '{') or \
                   (character == ']' and pending[-1] != '[') or \
                   (character == '>' and pending[-1] != '<') or \
                   (character == ')' and pending[-1] != '('):
                    print("Error in line {}, expected {} but got {}".format(line, pending[-1], character))
                    syntaxErrorScore += scoreTable[character]
                    corrupted = True
                    break
                else:
                    pending = pending[:-1]
                    
        if corrupted:
            continue
        autoCompletionScore = 0
        for character in pending[::-1]:
            autoCompletionScore *= 5
            autoCompletionScore += scoreTable[character]
        autoCompletionScores.append(autoCompletionScore)
        
    autoCompletionScores.sort()
        
    print("The total sytax error score is", syntaxErrorScore)
    print("The total auto-completion score is", autoCompletionScores[len(autoCompletionScores) // 2])
            