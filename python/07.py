class Dir(object):
    def __init__(self, name):
        self.name = name
        self.childDirs = {}
        self.parentDir = None
        self.files = {}
        self.sum = 0

    def calcSum(self):
        self.sum = 0
        for child in self.childDirs:
            self.childDirs[child].calcSum()
            self.sum +=  self.childDirs[child].sum
        for file in self.files:
            self.sum += self.files[file]

    def __repr__(self) -> str:
        return f"{type(self).__name__}(name: {self.name}, sum: {self.sum})"

f = open("/Users/jo/development/adventOfCode22/input/07.txt", "r")
lines = f.readlines()

root = Dir('/')
actDir = root

for line in lines:
    line = line.split()
    if line[0] == '$':
        #command
        if line[1] == 'cd':
            if line[2] == '/':
                continue
            if line[2] == '..':
                actDir = actDir.parentDir
                continue
            actDir.childDirs[line[2]].parentDir = actDir
            actDir = actDir.childDirs[line[2]]
    elif line[0] == 'dir':
        actDir.childDirs[line[1]] = Dir(line[1])
    else:
        actDir.files[line[1]] = int(line[0])


dirs = []

def calcChilds(dir):
    if dir.childDirs:
        for child in dir.childDirs:
            calcChilds(dir.childDirs[child])
    dir.calcSum()
    dirs.append(dir)

calcChilds(root)

freeSpace = 70000000 - dirs[-1].sum
neededSpace = 30000000 - freeSpace

bestTake = dirs[-1]
for dir in dirs[:-1]:
    if abs(neededSpace - dir.sum) < abs(neededSpace - bestTake.sum):
        bestTake = dir

print(bestTake)
