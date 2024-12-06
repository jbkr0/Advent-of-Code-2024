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

map[start[0]][start[1]] = 'X'

def isExitMap(x, y):
    return x < 0 or y < 0 or x >= len(map) or y >= len(map[0])

def getForward(x, y, direction):
    if direction == '^':
        return (x - 1, y)
    elif direction == '>':
        return (x, y + 1)
    elif direction == 'v':
        return (x + 1, y)
    elif direction == '<':
        return (x, y - 1)

while True:
    nextmove = getForward(start[0], start[1], curDirection)
    if (isExitMap(nextmove[0], nextmove[1])):
        break
    if map[nextmove[0]][nextmove[1]] == '#':
        curDirection = directions[(directions.index(curDirection) + 1) % 4]
        continue
    map[nextmove[0]][nextmove[1]] = 'X'
    start = nextmove

open('output.txt', 'w').write('\n'.join(''.join(row) for row in map))

print(sum(row.count('X') for row in map))


