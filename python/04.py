f = open("/Users/jo/development/adventOfCode22/input/04.txt", "r")
lines = f.readlines()

count = 0

for line in lines:
    ranges = []
    for elf in line.split(','):
        part = elf.split('-')
        parts = [*range(int(part[0]), int(part[1])+1)]
        ranges.append(parts)
        
    first = [g for g in ranges[0] if g in ranges[1]]
    sec = [g for g in ranges[1] if g in ranges[0]]



    if len(first) > 0 or len(sec) > 0:
        count += 1

print('count', count)