import re
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

def nb_robots(x, y):
    count = 0
    for robot in robots:
        if robot[0] == x and robot[1] == y:
            count += 1
    return count

for s in range(100):
    for robot in robots:
        robot[0] = (robot[0] + robot[2]) % width
        robot[1] = (robot[1] + robot[3]) % height

up_right = 0
up_left = 0
down_right = 0
down_left = 0

for y in range(height):
    for x in range(width):
        if y < mid_height and x < mid_width:
            up_left += nb_robots(x, y)
        elif y < mid_height and x > mid_width:
            up_right += nb_robots(x, y)
        elif y > mid_height and x < mid_width:
            down_left += nb_robots(x, y)
        elif y > mid_height and x > mid_width:
            down_right += nb_robots(x, y)

print(f"up_right: {up_right}, up_left: {up_left}, down_right: {down_right}, down_left: {down_left}")

print(up_right * up_left * down_right * down_left)