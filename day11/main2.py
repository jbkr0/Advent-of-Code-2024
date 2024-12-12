import math
from collections import defaultdict

with open('input.txt', 'r') as fichier:
    stones = [int(x) for x in fichier.readline().strip().split()]

def digit_count(stone):
    return int(math.log10(stone)) + 1 if stone > 0 else 1

def init_stones(stones, stones_count):
    for stone in stones:
        stones_count[stone] += 1

def blink(stones, iteration):
    stones_count = defaultdict(int)

    init_stones(stones, stones_count)

    for _ in range(iteration):
        for nb, count in list(stones_count.items()):
            if count == 0:
                continue
            if nb == 0:
                stones_count[0] -= count
                stones_count[1] += count
                continue
            nb_digits = digit_count(nb)
            if nb_digits % 2 == 0:
                divisor = 10 ** (nb_digits // 2)
                stones_count[nb // divisor] += count
                stones_count[nb % divisor] += count
                stones_count[nb] -= count
            else:
                stones_count[nb * 2024] += count
                stones_count[nb] -= count
    return sum(stones_count.values())

print(blink(stones, 75))