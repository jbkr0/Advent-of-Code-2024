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

