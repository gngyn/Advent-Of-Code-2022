dictMoves = {('A', 'X'): 3, ('A', 'Y'): 6, ('A', 'Z'): 0, ('B', 'X'): 0, ('B', 'Y'): 3, ('B', 'Z'): 6, ('C', 'X'): 6,
    ('C', 'Y'): 0, ('C', 'Z'): 3, 'X': 1, 'Y': 2, 'Z': 3}

with open('input.txt') as file:
    totalScore = 0
    
    for move in file:
        round = move.split()
        
        totalScore += dictMoves[tuple(round)]
        totalScore += dictMoves[round[1]]
        
    print(totalScore)
        