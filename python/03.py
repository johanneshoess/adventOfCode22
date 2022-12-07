import string

value = dict(zip(string.ascii_lowercase + string.ascii_uppercase, range(1,53)))

f = open("/Users/jo/development/adventOfCode22/input/03.txt", "r")
lines = f.readlines()


def splitLine(line):
    line = line.strip("\n")
    half = int(len(line)/2)
    return [line[0:half], line[half:]]   

prios = 0

for line in lines:
    halfs = splitLine(line)
    doub = set(halfs[0]).intersection(halfs[1]).pop()
    prios += value[doub]    

print("priority", prios)

#groups

index = 0
groupPrio = 0
while index < len(lines):
    group = lines[index:index+3]
    index += 3
    group[0] = group[0].split('\n')[0]
    inter = set(group[0]).intersection(set(group[1]), set(group[2])).pop()
    if len(inter) > 0 and inter != '\n':
        groupPrio += value[inter]

print("groupPrio", groupPrio)



