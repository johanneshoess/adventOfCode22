stacks = {
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [],
    9: []
}

f = open("/Users/jo/development/adventOfCode22/input/05.txt", "r")
lines = f.readlines()

for line in reversed(lines[:8]): # anzahl anpassen -> 8/3
    if line[1] != ' ':
        stacks[1].append(line[1])
    if line[5] != ' ':
        stacks[2].append(line[5])
    if line[9] != ' ':
        stacks[3].append(line[9])
    if line[13] != ' ':
        stacks[4].append(line[13])
    if line[17] != ' ':
        stacks[5].append(line[17])
    if line[21] != ' ':
        stacks[6].append(line[21])
    if line[25] != ' ':
        stacks[7].append(line[25])
    if line[29] != ' ':
        stacks[8].append(line[29])
    if line[33] != ' ':
        stacks[9].append(line[33])

print(stacks)

for line in lines[10:]: #anzahl anpassen -> 10/5
    line = line.split()

    for x in stacks[int(line[3])][-int(line[1]):]:
        stacks[int(line[5])].append(x)
        stacks[int(line[3])].pop()

    # for i in range(int(line[1])):
    #     stacks[int(line[5])].append(stacks[int(line[3])].pop())

print("".join([stack.pop() for stack in stacks.values() if len(stack) > 0]))
