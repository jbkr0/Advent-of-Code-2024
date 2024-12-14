
from time import sleep
from enum import Enum

class Direction(Enum):
    RIGHT = 0
    LEFT = 1
    DOWN = 2
    UP = 3

with open('input.txt', 'r') as fichier:
    map = [list(line) for line in fichier.read().split('\n')]
height = len(map)
width = len(map[0])

def count_island(c, i, j, path) -> list:
    if (i, j) in path:
        return []
    island = []
    island.append((i, j))
    path.add((i, j))

    if j + 1 < width and map[i][j + 1] == c:
        sub_island = count_island(c, i, j + 1, path)
        island.extend(sub_island)
    if j - 1 >= 0 and map[i][j - 1] == c:
        sub_island = count_island(c, i, j - 1, path)
        island.extend(sub_island)
    if i + 1 < height and map[i + 1][j] == c:
        sub_island = count_island(c, i + 1, j, path)
        island.extend(sub_island)
    if i - 1 >= 0 and map[i - 1][j] == c:
        sub_island = count_island(c, i - 1, j, path)
        island.extend(sub_island)
    return island

def get_island():
    path = set()
    islands = []
    for i in range(height):
        for j in range(width):
            if (i, j) in path:
                continue
            island = count_island(map[i][j], i, j, path)
            islands.append(island)
    return islands

def count_side(islands):
    count = 0
    for island in islands:

        nb_sides = 0
        layers = {}
        for i, j in island:
            if i not in layers:
                layers[i] = []
            layers[i].append((i, j))

        # count top side
        last_line = []
        for _, layer in sorted(layers.items(), key=lambda x: x[0]):

            layer_side = []
            for i, j in layer:
                if (i - 1, j) in last_line:
                    continue
                layer_side.append((i, j))

            last_j = -2
            for _, j in sorted(layer_side, key=lambda x: x[1]):
                if j != last_j + 1:
                    nb_sides += 1
                last_j = j

            last_line.clear()
            for e in layer:
                last_line.append(e)

        # count bottom side
        last_line = []
        for _, layer in sorted(layers.items(), key=lambda x: x[0], reverse=True):
            layer_side = []
            for i, j in layer:
                if (i + 1, j) in last_line:
                    continue
                layer_side.append((i, j))

            last_j = -2
            for _, j in sorted(layer_side, key=lambda x: x[1]):
                if j != last_j + 1:
                    nb_sides += 1
                last_j = j

            last_line.clear()
            for e in layer:
                last_line.append(e)

        layers = {}
        for i, j in island:
            if j not in layers:
                layers[j] = []
            layers[j].append((i, j))

        # count left side
        last_line = []
        for _, layer in sorted(layers.items(), key=lambda x: x[0]):

            layer_side = []
            for i, j in layer:
                if (i, j - 1) in last_line:
                    continue
                layer_side.append((i, j))

            last_i = -2
            for i, _ in sorted(layer_side, key=lambda x: x[0]):
                if i != last_i + 1:
                    nb_sides += 1
                last_i = i

            last_line.clear()
            for e in layer:
                last_line.append(e)

        # count right side
        last_line = []
        for _, layer in sorted(layers.items(), key=lambda x: x[0], reverse=True):

            layer_side = []
            for i, j in layer:
                if (i, j + 1) in last_line:
                    continue
                layer_side.append((i, j))

            last_i = -2
            for i, _ in sorted(layer_side, key=lambda x: x[0]):
                if i != last_i + 1:
                    nb_sides += 1
                last_i = i

            last_line.clear()
            for e in layer:
                last_line.append(e)

        count += len(island) * nb_sides
    return count

islands = get_island()
print(count_side(islands))
