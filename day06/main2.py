import re

with open('input.txt', 'r') as fichier:
    map = [list(line) for line in fichier.read().split('\n')]

start = None
curDirection = '^'
directions = ['^', '>', 'v', '<']

for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] in directions:
            start = (i, j)
            curDirection = map[i][j]

def isExitMap(x, y):
    return x < 0 or y < 0 or x >= len(map) - 1 or y >= len(map[0]) - 1

def getForward(x, y, direction):
    if direction == '^':
        return (x - 1, y)
    elif direction == '>':
        return (x, y + 1)
    elif direction == 'v':
        return (x + 1, y)
    elif direction == '<':
        return (x, y - 1)
    
r = 0


for i in range(len(map)):
    for j in range(len(map[i])):
        curDirection = map[start[0]][start[1]]
        curPos = start

        loop_detec = set()
        while True:
            loop_detec.add((curPos, curDirection))

            nextmove = getForward(curPos[0], curPos[1], curDirection)
            if (isExitMap(nextmove[0], nextmove[1])):
                break

            if map[nextmove[0]][nextmove[1]] == '#' or nextmove == (i, j):
                curDirection = directions[(directions.index(curDirection) + 1) % 4]
            else:
                curPos = nextmove

            if (curPos, curDirection) in loop_detec:
                r += 1
                break


print(r)