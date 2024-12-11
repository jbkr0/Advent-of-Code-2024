
with open('input.txt', 'r') as fichier:
    stones = [int(x) for x in fichier.readline().strip().split()]

def blink(stones):
    new_stones = []
    for stone in stones:
        str_stone = str(stone)
        mid = len(str_stone) // 2

        if stone == 0:
            new_stones.append(1)
        elif len(str_stone) % 2 == 0:
            new_stones.append(int(str_stone[:mid]))
            new_stones.append(int(str_stone[mid:]))
        else:
            new_stones.append(stone * 2024)
    return new_stones

for _ in range(25):
    stones = blink(stones)

print(len(stones))