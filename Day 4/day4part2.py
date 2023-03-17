def makeList(pair):
    result = set()
    for i in range(pair[0], pair[1] + 1):
        result.add(i)
        
    return result

cnt = 0

with open('input.txt') as file:
    for pair in file:
        pair = pair.strip().split(',')
        pair1 = makeList(list(map(int, pair[0].split('-'))))
        pair2 = makeList(list(map(int, pair[1].split('-'))))
        
        contains = pair1 & pair2
        
        if len(contains) > 0:
            cnt += 1
            
print(cnt)