sum = 0

with open('input.txt') as file:
    sacks = []
    for rucksack in file:
        sacks.append(rucksack.strip('\n'))
        if len(sacks) == 3:
            item = list(set(sacks[0]) & set(sacks[1]) & set(sacks[2]))[0]
                
            if item.islower():
                sum += ord(item) - 96
            else:
                sum += ord(item) - 38
                
            sacks = []
            
print(sum)