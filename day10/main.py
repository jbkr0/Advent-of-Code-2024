import re

from enum import Enum

with open('input.txt', 'r') as fichier:
    map = [list(line) for line in fichier.read().split('\n')]

width = len(map[0])
height = len(map)

start = set()

for i in range(height):
    for j in range(width):
        if map[i][j] == '0':
            start.add((i, j))

def posInMap(x, y):
    return x >= 0 and x < height and y >= 0 and y < width

def findHikingTrail(pos, nb, r : set):
    if nb == '9':
        r.add(pos)
        return
    nextnb = chr(ord(nb) + 1)
    if posInMap(pos[0], pos[1] + 1) and map[pos[0]][pos[1] + 1] == nextnb:
        findHikingTrail((pos[0], pos[1] + 1), nextnb, r)
    if posInMap(pos[0], pos[1] - 1) and map[pos[0]][pos[1] - 1] == nextnb:
        findHikingTrail((pos[0], pos[1] - 1), nextnb, r)
    if posInMap(pos[0] + 1, pos[1]) and map[pos[0] + 1][pos[1]] == nextnb:
        findHikingTrail((pos[0] + 1, pos[1]), nextnb, r)
    if posInMap(pos[0] - 1, pos[1]) and map[pos[0] - 1][pos[1]] == nextnb:
        findHikingTrail((pos[0] - 1, pos[1]), nextnb, r)

r = 0

for pos in start:
    pos9 = set()
    findHikingTrail(pos, '0', pos9)
    r += len(pos9)

print(r)