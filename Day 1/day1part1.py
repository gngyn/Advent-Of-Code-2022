max = 0
currentCnt = 0
with open('input.txt') as file:
    for value in file:
        if (value != '\n'):
            currentCnt += int(value)
        else:
            if (currentCnt > max):
                max = currentCnt
            currentCnt = 0       
print(max)