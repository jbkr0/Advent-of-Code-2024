
with open('input.txt', 'r') as fichier:
    map = [list(line) for line in fichier.read().split('\n')]
height = len(map)
width = len(map[0])

def count_price(c, i, j, path):
    if (i, j) in path:
        return 0, 0
    path.add((i, j))
    count = 1
    perimeter = 0

    if j + 1 >= width or map[i][j + 1] != c:
        perimeter += 1
    if j - 1 < 0 or map[i][j - 1] != c:
        perimeter += 1
    if i + 1 >= height or map[i + 1][j] != c:
        perimeter += 1
    if i - 1 < 0 or map[i - 1][j] != c:
        perimeter += 1

    if j + 1 < width and map[i][j + 1] == c:
        sub_count, sub_perimeter = count_price(c, i, j + 1, path)
        count += sub_count
        perimeter += sub_perimeter
    if j - 1 >= 0 and map[i][j - 1] == c:
        sub_count, sub_perimeter = count_price(c, i, j - 1, path)
        count += sub_count
        perimeter += sub_perimeter
    if i + 1 < height and map[i + 1][j] == c:
        sub_count, sub_perimeter = count_price(c, i + 1, j, path)
        count += sub_count
        perimeter += sub_perimeter
    if i - 1 >= 0 and map[i - 1][j] == c:
        sub_count, sub_perimeter = count_price(c, i - 1, j, path)
        count += sub_count
        perimeter += sub_perimeter
    return count, perimeter

path = set()
r = 0

for i in range(height):
    for j in range(width):
        if (i, j) in path:
            continue
        count, perimeter = count_price(map[i][j], i, j, path)
        r += count * perimeter

print(r)