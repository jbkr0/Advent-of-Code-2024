import re
import numpy as np
from collections import defaultdict

with open('input.txt', 'r') as fichier:
    file = fichier.read()
matches = re.findall(r"p=(\d+),(\d+)\s+v=(-?\d+),(-?\d+)", file)
height = 103
width = 101
mid_height = height // 2
mid_width = width // 2

robots = []

for match in matches:
    robots.append([int(match[0]), int(match[1]), int(match[2]), int(match[3])])

# def nb_robots(x, y):
#     count = 0
#     for robot in robots:
#         if robot[0] == x and robot[1] == y:
#             count += 1
#     return count

# def count_price(map, i, j, path) -> int:
#     if (i, j) in path:
#         return 0
#     path.add((i, j))
#     count = 1

#     if j + 1 < width and map[i][j + 1] > 0:
#         count += count_price(map, i, j + 1, path)
#     if j - 1 >= 0 and map[i][j - 1] > 0:
#         count += count_price(map, i, j - 1, path)
#     if i + 1 < height and map[i + 1][j] > 0:
#         count += count_price(map, i + 1, j, path)
#     if i - 1 >= 0 and map[i - 1][j] > 0:
#         count += count_price(map, i - 1, j, path)
#     return count

def create_robot_positions():
    positions = defaultdict(list)
    for idx, robot in enumerate(robots):
        positions[(robot[0], robot[1])].append(idx)
    return positions

def nb_robots(x, y, robot_positions):
    return len(robot_positions.get((x, y), []))

def create_map(robot_positions):
    map_array = np.zeros((height, width), dtype=int)
    for (x, y), robots_at_pos in robot_positions.items():
        map_array[y, x] = len(robots_at_pos)
    return map_array

def count_price(map_array, i, j, visited):
    if not (0 <= i < height and 0 <= j < width) or visited[i,j] or map_array[i,j] == 0:
        return 0
    visited[i,j] = True
    count = 1
    for di, dj in [(0,1), (0,-1), (1,0), (-1,0)]:
        count += count_price(map_array, i + di, j + dj, visited)
    return count

def is_Easter_Egg():
    robot_positions = create_robot_positions()
    map_array = create_map(robot_positions)
    visited = np.zeros((height, width), dtype=bool)

    for i in range(height):
        for j in range(width):
            if not visited[i][j] and map_array[i][j] > 0:
                if count_price(map_array, i, j, visited) > 20:
                    return True
    return False

def print_robots():
    robot_positions = set((robot[0], robot[1]) for robot in robots)
    grid = [['X' if (x,y) in robot_positions else '.' for x in range(width)] for y in range(height)]
    with open('output.txt', 'w') as output:
        output.write('\n'.join(''.join(row) for row in grid))

i = 0
while True:
    _ = input()
    while True:
        print(i + 1)
        for robot in robots:
            robot[0] = (robot[0] + robot[2]) % width
            robot[1] = (robot[1] + robot[3]) % height
        i += 1
        if is_Easter_Egg():
            break
    print_robots()

