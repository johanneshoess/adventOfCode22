f = open("../input/01.txt", "r")
lines = f.readlines()

elfes = []
count = 0
for line in lines:
    if line == "\n":
        elfes.append(count)
        count = 0
    else:
        line = int(line)
        count += line

elfes.sort()
print(elfes[-1]+elfes[-2]+elfes[-3])
