import re

r = 0

def check_direction(grid, x, y, dx, dy, word):
    if not (0 <= x + dx * (len(word) - 1) < len(grid) and 0 <= y + dy * (len(word) -1 ) < len(grid[0])):
        return False
    return all(grid[x + dx * i][y + dy * i] == word[i] for i in range(len(word)))

with open('input.txt', 'r') as fichier:
    map = [line.strip() for line in fichier.readlines()]
    directions = [(0,1), (1,0), (1,1), (-1,1), (0,-1), (-1,0), (-1,-1), (1,-1)]

    word = "XMAS"
    word_reversed = word[::-1]

    for i in range(len(map)):
        for j in range(len(map[0])):
            for dx, dy in directions:
                if check_direction(map, i, j, dx, dy, word):
                    r += 1

print(r)