import re

with open('input.txt', 'r') as fichier:
    file = fichier.read().strip()

map = [list(line) for line in re.findall(r"([#O.@]+)", file) if line.strip()]
directions = ''.join(re.findall(r"([v><^]+)", file, re.MULTILINE))

height = len(map)
width = len(map[0])
pos = (0, 0)

for i in range(height):
    for j in range(width):
        if map[i][j] == "@":
            pos = (i, j)
            break

def can_push(d, x, y):
    if map[y][x] == "#":
        return False
    if map[y][x] == "O":
        return can_push(d, x + d[0], y + d[1])
    return True

def move(c, pos):
    switcher = {
        "^": (0, -1),
        "v": (0, 1),
        "<": (-1, 0),
        ">": (1, 0)
    }
    d = switcher[c]

    x = pos[0] + d[0]
    y = pos[1] + d[1]

    if can_push(d, x, y):
        block = False
        if map[y][x] == "O":
            block = True
        map[y][x] = "@"
        map[pos[1]][pos[0]] = "."
        pos = (x, y)
        x += d[0]
        y += d[1]
        while map[y][x] != '.' and map[y][x] != '#':
            map[y][x] = "O"
            x += d[0]
            y += d[1]
        if block:
            map[y][x] = "O"
    return pos

for d in directions:
    pos = move(d, pos)

r = 0
for i in range(height):
    for j in range(width):
        if map[i][j] != "O":
            continue
        r += i * 100 + j

print(r)