f = open("/Users/jo/development/adventOfCode22/input/06.txt", "r")
lines = f.readlines()

for line in lines:
    for i in range(len(line)):
        if len(set(line[i:i+14])) == 14:
            print(i+14)
            print(line[i:i+14])
            break