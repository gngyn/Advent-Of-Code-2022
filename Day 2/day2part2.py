dictMoves = {('A', 'X'): 3, ('A', 'Y'): 4, ('A', 'Z'): 8, ('B', 'X'): 1, ('B', 'Y'): 5, ('B', 'Z'): 9, ('C', 'X'): 2,
    ('C', 'Y'): 6, ('C', 'Z'): 7}

with open('input.txt') as file:
    totalScore = 0
    
    for move in file:
        round = move.split()
        
        totalScore += dictMoves[tuple(round)]
        
    print(totalScore)