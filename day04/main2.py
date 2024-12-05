def check_x(grid, x, y):
    if not (0 <= x-1 < len(grid) and 0 <= x+1 < len(grid) and
            0 <= y-1 < len(grid[0]) and 0 <= y+1 < len(grid[0])):
        return False

    patterns = [
        # Pattern normal MAS
        [((-1,-1,'M'), (1,1,'S'), (-1,1,'M'), (1,-1,'S')),
         ((-1,-1,'S'), (1,1,'M'), (-1,1,'S'), (1,-1,'M'))],
        # Pattern inversé
        [((-1,-1,'S'), (1,1,'M'), (-1,1,'S'), (1,-1,'M')),
         ((-1,-1,'M'), (1,1,'S'), (-1,1,'M'), (1,-1,'S'))],
        # Pattern horizontal
        [((-1,-1,'S'), (1,1,'M'), (-1,1,'M'), (1,-1,'S')),
         ((-1,-1,'M'), (1,1,'S'), (-1,1,'S'), (1,-1,'M'))],
        # Pattern vertical
        [((-1,-1,'S'), (1,1,'M'), (-1,1,'M'), (1,-1,'S')),
         ((-1,-1,'M'), (1,1,'S'), (-1,1,'S'), (1,-1,'M'))]
    ]

    if grid[x][y] != 'A':
        return False

    for pattern_group in patterns:
        for pattern in pattern_group:
            if all(grid[x + dx][y + dy] == val
                  for dx, dy, val in pattern):
                return True

    return False

r = 0
with open('input.txt', 'r') as fichier:
    map = [line.strip() for line in fichier.readlines()]

    for i in range(len(map)):
        for j in range(len(map[0])):
            if (check_x(map, i, j)):
                r += 1

print(r)