# A -> Stein -> X -> 1 Points
# B -> Paper -> Y -> 2 Points
# C -> Schere -> Z -> 3 Points
# 0 Points if you lose, 3 for draw and 6 if win

# X -> lose
# Y -> draw
# Z -> win

getSlayed = {
    "A": "B",
    "B": "C",
    "C": "A" 
}

slay = {
    "A": "C",
    "B": "A",
    "C": "B"
}

f = open("/Users/jo/development/adventOfCode22/input/02.txt", "r")
lines = f.readlines()

def takeHand(hand):
    if hand[1] == "X":
        hand[1] = slay[hand[0]]
    elif hand[1] == "Y":
        hand[1] = hand[0]
    elif hand[1] == "Z":
        hand[1] = getSlayed[hand[0]]
        
def calcPoints(line):
    hand = line.split()
    takeHand(hand)
    if getSlayed[hand[0]] == hand[1]:
        return 6 + list(slay).index(hand[1]) + 1
    elif hand[0] == hand[1]:
        return 3 + list(slay).index(hand[1]) + 1
    else:
        return list(slay).index(hand[1]) + 1

points = 0

for line in lines:
    points += calcPoints(line)
    print("round", points)
    
print('Points:', points)