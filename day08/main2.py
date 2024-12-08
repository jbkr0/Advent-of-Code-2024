import re

with open('input.txt', 'r') as fichier:
    map = [list(line) for line in fichier.read().split('\n')]
height = len(map)
width = len(map[0])
antennas = dict()
output = [['.' for _ in range(width)] for _ in range(height)]

for i in range(height):
    for j in range(width):
        c = map[i][j]
        if c in antennas:
            antennas[c].append((i,j))
        else:
            antennas[c] = [(i,j)]
antennas.pop('.')

def isValide(x, y) -> bool:
    return 0 <= x < len(map) and 0 <= y < len(map[0])

def find_antinode(pos1, center):
    x = 2 * center[0] - pos1[0]
    y = 2 * center[1] - pos1[1]
    return (x, y)

def evalAntinodes(antenna) -> int:

    for pos1 in antenna:
        for pos2 in antenna:
            if pos1 == pos2:
                continue

            start = pos1
            center = pos2
            output[center[0]][center[1]] = '#'
            antinode = find_antinode(start, center)
            while isValide(*antinode):
                output[antinode[0]][antinode[1]] = '#'
                start = center
                center = antinode
                antinode = find_antinode(start, center)

for antenna in antennas.values():
    evalAntinodes(antenna)
print(sum(line.count('#') for line in output))
