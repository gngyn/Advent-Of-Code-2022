max1, max2, max3 = 0,0,0
currentCnt = 0

with open('input.txt') as file:
    for value in file:
        if (value != '\n'):
            currentCnt += int(value)
        else:
            if (currentCnt > max1):
                max3 = max2
                max2 = max1
                max1 = currentCnt
            elif (currentCnt > max2):
                max3 = max2
                max2 = currentCnt
            elif (currentCnt > max3):
                max3 = currentCnt
            
            currentCnt = 0       
print(max1 + max2 + max3)
