def find(first, second):
    result = ''
    
    for i in first:
        for j in second:
            if j == i:
                result = i
                
    return result

sum = 0

with open('input.txt') as file:
    for rucksack in file:
        length = int(len(rucksack) / 2)
        item = find(rucksack[:length], rucksack[length:])
        
        if item.islower():
            sum += ord(item) - 96
        else:
            sum += ord(item) - 38
            
print(sum)
        
        
        
        
        