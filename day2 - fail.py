## Day 2
data = open("input.txt", "r")
file = data.read()

empty = []
others = []
winners = []
rock = 1
paper = 2
scissors = 3
loss = 0
win = 6
draw = 3

for line in file.splitlines():
    empty.append(line)

for x in range(len(empty)):
    firstChar = empty[x][0]
    lastChar = empty[x][2]
    others.append(firstChar)
    winners.append(lastChar)

score = 0

for i in range(len(empty)):
    if winners[i-1] == 'Y': # paper
        score = score + 3
        if others[i-1] == 'C':
            score = score + 6
        elif others[i-1] == 'B':
            score = score + 3
    elif winners[i-1] == 'X': #rock
        score = score + 1
        if others[i-1] == 'B':
            score = score + 6
        elif others[i-1] == 'A':
            score = score + 3
    elif winners[i-1] == 'Z': #scissors
        score = score + 2
        if others[i-1] == 'A':
            score = score + 6
        elif others[-1] == 'C':
            score = score + 3
    
print(score)
