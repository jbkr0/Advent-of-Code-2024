import re

with open('input.txt', 'r') as fichier:
    disk_map = fichier.readline().strip()

def decompress(disk_map) -> list:
    result = []
    id = 0
    isSpace = False
    for c in disk_map:
        for _ in range(int(c)):
            result.append(-1 if isSpace else id)
        if not isSpace:
            id += 1
        isSpace = False if isSpace else True
    return result

def compact(disk_map : list) -> list:
    start = 0
    end = len(disk_map)
    while start < end:
        if disk_map[start] != -1:
            start += 1
            continue
        while end > start and disk_map[end - 1] == -1:
            end -= 1
            disk_map.pop()
        if end > start:
            end -= 1
            disk_map[start] = disk_map[end]
            disk_map.pop()
    return disk_map

def filesystem_checksum(disk_map : str) -> int:
    r = 0
    for i in range(len(disk_map)):
        r += i * disk_map[i]
    return r

print(filesystem_checksum(compact(decompress(disk_map))))
